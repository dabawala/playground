from rev_ai import apiclient
from rev_ai.models.asynchronous.job_status import JobStatus
import time
import pyaudio
import wave
import threading
import openai
from typing import *

token = "02mq7zrp5cOEKStOjfr2-yt_K21aBr4mJVnvLkcpsrK8I7EOKVz7Qh6KI6EI8YSL_tKXy2OaVKjhhr7x41AalUQ9hpkTk"


class Transcriber:
    def __init__(self, on_finish: Callable, on_error: Callable):
        self.transcript = []
        self.job = None
        self.stream = None
        self._record = False
        self.client = apiclient.RevAiAPIClient(token)
        self.lock = threading.Lock()
        self.on_finish = on_finish
        self.on_error = on_error

    @property
    def is_transcribing(self):
        return (self.job is not None
                and self.client.get_job_details(self.job.id).status == JobStatus.IN_PROGRESS)

    @property
    def is_recording(self):
        return self._record
    
    def start(self,
              chunk=1024,
              sample_format=pyaudio.paInt16,
              channels=2,
              rate=8000):
        if self.is_recording:
            raise RuntimeError("Already recording")
        p = pyaudio.PyAudio()
        def loop():
            self.lock.acquire()
            print("Lock acquired")
            self._record = True
            self.stream = p.open(format=sample_format,
                                 channels=channels,
                                 rate=rate,
                                 frames_per_buffer=chunk,
                                 input=True)
            frames = []
            while self._record:
                data = self.stream.read(chunk)
                frames.append(data)
            self.stream.stop_stream()
            self.stream.close()
            p.terminate()
            filename = f"/tmp/{time.time()}.wav"
            wf = wave.open(filename, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(sample_format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            # now transcribe it!
            """
            self.job = self.client.submit_job_local_file(filename)
            print(f"Submitted job {self.client.get_job_details(self.job.id).status}")
            while self.client.get_job_details(self.job.id).status == JobStatus.IN_PROGRESS:
                time.sleep(0.5)
            job_status = self.client.get_job_details(self.job.id).status
            print(f"Job {self.job.id} finished with status {job_status}")
            if job_status == JobStatus.TRANSCRIBED:
                self.on_finish(self.client.get_transcript_text(self.job.id))
            else:
                self.on_error(self.job)
            """
            audio_file = open(filename, "rb")
            self.on_finish(openai.Audio.transcribe("whisper-1", audio_file).get("text", "Could not transcribe"))
            self.lock.release()
        threading.Thread(target=loop).start()
        #loop()
    
    def stop(self):
        if not self._record:
            raise RuntimeError("Not recording")
        self._record = False

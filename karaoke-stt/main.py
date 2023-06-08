from rev_ai import apiclient
from rev_ai.models.asynchronous.job_status import JobStatus
import time

token = "02mq7zrp5cOEKStOjfr2-yt_K21aBr4mJVnvLkcpsrK8I7EOKVz7Qh6KI6EI8YSL_tKXy2OaVKjhhr7x41AalUQ9hpkTk"
client = apiclient.RevAiAPIClient(token)
job = client.submit_job_local_file("C:\\test2.mp3")
while client.get_job_details(job.id).status != JobStatus.TRANSCRIBED: # not transcribed
    print("not done yet")
    time.sleep(1)
print("transcribed")
transcript_text = client.get_transcript_text(job.id)
print(transcript_text)

# Smart Bus Station Voice Assistant Dabawala

The Smart Bus Station Voice Assistant is an intelligent system designed to provide information and answer questions related to bus stations. It leverages voice input and natural language processing techniques to understand user queries and provides spoken responses in return. This project aims to enhance the user experience and provide a convenient way to interact with bus station information.

![Flowchart](diagram.png)

## Features

- Voice Input: Users can ask questions or provide queries using natural speech.
- Natural Language Processing: The system utilizes NLP techniques to understand and interpret user queries accurately.
- Information Retrieval: It retrieves relevant information about bus stations, such as bus schedules, routes, delays, and more.
- Spoken Responses: The system provides spoken responses to users, making it easy to interact and receive information hands-free.
- Real-time Updates: It can provide real-time updates on bus arrivals, departures, and any changes in schedules.

## How It Works

The Smart Bus Station Voice Assistant combines various technologies to deliver its functionality:

1. Speech Recognition: The system utilizes speech recognition techniques to convert user's spoken queries into text format.
2. Natural Language Understanding: It employs natural language understanding and interpret user queries using ChatGPT, extracting the intent and relevant parameters. 
3. Information Retrieval: The system queries a bus station information database to retrieve the requested information based on the user's query using googlemaps API.
4. Text-to-Speech Conversion: It uses text-to-speech synthesis to convert the response text into spoken form, allowing the system to provide spoken answers to the user's queries.

## Getting Started

To use the Smart Bus Station Voice Assistant, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/smart-bus-station.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the speech recognition and text-to-speech components according to the documentation of the chosen libraries or APIs.
4. Configure the bus station information database or API integration to retrieve relevant data.
5. Run the application: `python main.py`
6. Speak your queries and wait for the voice assistant to process and provide responses.

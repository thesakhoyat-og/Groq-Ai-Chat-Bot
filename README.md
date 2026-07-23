# Xender AI Chatbot

Xender is a simple terminal-based AI chatbot built with Python and the Groq API.

The chatbot takes user input from the terminal, sends the message to a Groq language model, receives a response, and prints the assistant's reply.

## Features

- Terminal-based chatbot
- Uses Groq API for AI responses
- Stores conversation messages in a list
- Sends user messages to the model
- Prints AI-generated responses
- Beginner-friendly Python AI project

## Technologies Used

- Python
- Groq API
- Llama 3.1 8B Instant model

## How the Code Works

1. The program imports the required libraries.
2. A Groq client is created using an API key.
3. A list called `messages` stores the conversation.
4. The user enters a question in the terminal.
5. The user's message is added to the `messages` list.
6. The message is sent to the Groq model.
7. The model returns a response.
8. The assistant's response is added to the conversation history.
9. The response is printed in the terminal.
    
##Current Limitations
Conversation history exists only while the program is running
Messages are not stored in a file or database
Long conversations may increase token usage
The chatbot requires an internet connection
The chatbot depends on Groq API availability
There is no graphical user interface
There is no user authentication
The chatbot does not currently support file uploads

Author 
Sakhoyat Hossain Siam

## Requirements

Before running this project, install the Groq Python package:



```bash
pip install groq


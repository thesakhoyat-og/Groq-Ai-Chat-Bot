# Xender AI Chatbot

Xender is a beginner-friendly, terminal-based AI chatbot built with Python and the Groq API.

The program accepts user input through the command line, sends the message to a Groq-hosted language model, receives an AI-generated response, and displays the result in the terminal.

It also maintains a conversation history, allowing the model to respond using the context of previous messages.

---

## Project Overview

Xender demonstrates how Python can be connected to a large language model through an external API.

The chatbot runs inside the terminal and uses a continuous input loop so users can have an ongoing conversation with the AI assistant.

Each user message and assistant response is stored in a list and sent back to the model with every request. This allows the chatbot to remember earlier parts of the conversation during the current session.

---

## Features

* Terminal-based chatbot interface
* AI-generated responses using the Groq API
* Continuous conversation loop
* Stores conversation history in a Python list
* Sends previous messages as context
* Uses user and assistant message roles
* Handles repeated user input
* Beginner-friendly project structure
* Fast responses using Groq-hosted language models

---

## Technologies Used

| Technology           | Purpose                                   |
| -------------------- | ----------------------------------------- |
| Python               | Main programming language                 |
| Groq API             | Sends prompts and receives AI responses   |
| Groq Python SDK      | Connects the Python application to Groq   |
| Llama 3.1 8B Instant | Language model used to generate responses |
| Terminal             | User interface for the chatbot            |

---

## How the Program Works

1. The required Groq library is imported.
2. A Groq client is created using an API key.
3. A list named `messages` stores the conversation history.
4. The chatbot waits for the user to enter a message.
5. The user's message is added to the `messages` list.
6. The complete conversation history is sent to the Groq model.
7. The model generates an assistant response.
8. The assistant response is added to the conversation history.
9. The response is printed in the terminal.
10. The process repeats until the user stops the program.

---

## Conversation History

Messages are stored using role-based dictionaries.

Example:

```python
messages = [
    {
        "role": "system",
        "content": "You are Xender, a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "What is Python?"
    },
    {
        "role": "assistant",
        "content": "Python is a high-level programming language."
    }
]
```

Each message contains:

* `role`: identifies who sent the message
* `content`: contains the actual message text

The supported roles are:

* `system`
* `user`
* `assistant`

The system message defines the chatbot's behaviour, while the user and assistant messages form the conversation history.

---

## Project Structure

```text
xender-ai-chatbot/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

| File               | Description                                  |
| ------------------ | -------------------------------------------- |
| `main.py`          | Contains the chatbot logic                   |
| `requirements.txt` | Lists the required Python packages           |
| `.env`             | Stores the Groq API key locally              |
| `.gitignore`       | Prevents sensitive files from being uploaded |
| `README.md`        | Contains project documentation               |

---

## Requirements

Before running the project, make sure the following are installed:

* Python 3.10 or newer
* A Groq account
* A Groq API key
* The Groq Python package

Install the Groq package using:

```bash
pip install groq
```

You can also create a `requirements.txt` file containing:

```text
groq
python-dotenv
```

Then install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## API Key Setup

The Groq API key should not be written directly inside the Python source code.

Create a file named `.env` in the project folder:

```text
GROQ_API_KEY=your_api_key_here
```

Install `python-dotenv`:

```bash
pip install python-dotenv
```

Load the environment variable in Python:

```python
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY was not found.")

client = Groq(api_key=api_key)
```

Add `.env` to the `.gitignore` file:

```text
.env
__pycache__/
*.pyc
```

This prevents the API key from being uploaded to GitHub.

---

## Example Chatbot Logic

```python
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY was not found.")

client = Groq(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are Xender, a helpful AI assistant."
    }
]

print("Xender: Hi, I am Xender. How may I help you?")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        print("Xender: Goodbye!")
        break

    if not user_input:
        continue

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        assistant_response = chat_completion.choices[0].message.content

        messages.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

        print(f"Xender: {assistant_response}")

    except Exception as error:
        print(f"An error occurred: {error}")
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/xender-ai-chatbot.git
```

### 2. Open the Project Folder

```bash
cd xender-ai-chatbot
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv env
env\Scripts\activate
```

#### macOS or Linux

```bash
python3 -m venv env
source env/bin/activate
```

### 4. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add the API Key

Create a `.env` file and add:

```text
GROQ_API_KEY=your_api_key_here
```

### 6. Run the Chatbot

```bash
python main.py
```

---

## Example Output

```text
Xender: Hi, I am Xender. How may I help you?

You: What is artificial intelligence?

Xender: Artificial intelligence is a field of computer science focused on
creating systems that can perform tasks that normally require human intelligence.

You: Give me an example.

Xender: A virtual assistant that understands questions and provides useful
responses is one example of artificial intelligence.

You: exit

Xender: Goodbye!
```

---

## Error Handling

The chatbot can include basic error handling for:

* Missing API keys
* Invalid API keys
* Network connection problems
* API request failures
* Empty user input
* Unexpected model responses

Using `try` and `except` prevents the program from crashing immediately when an API request fails.

---

## Security Notes

The API key must remain private.

Do not:

* Add the API key directly to `main.py`
* Upload the `.env` file to GitHub
* Share the API key in screenshots
* Add the API key to the README
* Commit the API key in previous Git history

Recommended practices:

* Store secrets in environment variables
* Add `.env` to `.gitignore`
* Revoke exposed API keys immediately
* Generate a new key if the old one becomes public
* Use separate keys for development and production

---

## Technical Concepts Demonstrated

This project demonstrates:

* Python input and output
* Variables and lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* API integration
* Environment variables
* Exception handling
* Conversation history management
* Object creation
* Accessing API response objects
* Working with external Python packages

---

## Current Limitations

* Conversation history exists only while the program is running
* Messages are not stored in a file or database
* Long conversations may increase token usage
* The chatbot requires an internet connection
* The chatbot depends on Groq API availability
* There is no graphical user interface
* There is no user authentication
* The chatbot does not currently support file uploads

---

## Future Improvements

Possible future improvements include:

* Save conversation history to a JSON file
* Add commands to clear the conversation
* Limit the number of stored messages
* Add coloured terminal output
* Add response streaming
* Add multiple AI personalities
* Allow users to choose a model
* Add voice input and speech output
* Build a graphical interface using Tkinter
* Build a web interface using Flask
* Store conversations in a database
* Add automated tests
* Add logging
* Add custom system prompts
* Add chat export functionality

---

## Author

Md Sakhoyat Hossain Siam

---

## License

This project was created for educational and portfolio purposes.

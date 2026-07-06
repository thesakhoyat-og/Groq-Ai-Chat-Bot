import os
from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

messages=[]




def completion(message):
    global messages
    
    messages.append(  
        {
            "role":"user",
            "content": message,
        }
    )
    chat_completion = client.chat.completions.create( messages = messages,model="llama-3.1-8b-instant" 
    )
    print(chat_completion)
    message = {
        "role" : "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Xender: {message['content']}")

if __name__ == "__main__":
    user_question = input(f"Xender: Hi, I am Xender, How may i help you ? \n>>>")
    completion(user_question)
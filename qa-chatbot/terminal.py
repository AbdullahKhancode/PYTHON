import google.generativeai as genai
import os 
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")




while True:
    user_input=input("You: Enter your question(type exit, quit, or bye to end the conversation): ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Thank you for using the chatbot! Goodbye!")
        break
    response = model.generate_content(user_input)
    print(response.text)

    













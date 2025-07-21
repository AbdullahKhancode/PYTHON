import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv  

load_dotenv()
gemini_api_key=os.getenv("GOOGLE_API_KEY")
model=genai.GenerativeModel("gemini-2.0-flash")
@cl.on_chat_start
async def start():
   await cl.Message(content="Hello! I'm your AI assistant. How can I help you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
   prompt=message.content
   response=model.generate_content(prompt)
   response_text=response.text if hasattr(response, "text") else "Sorry, I couldn't generate a response."
   await cl.Message(content=response_text).send()

   
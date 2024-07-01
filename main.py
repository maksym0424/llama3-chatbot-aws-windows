import os
import torch
import transformers
from llms.llama3 import Llama3
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Dict, Any

load_dotenv()

# init
hf_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
model = Llama3(access_token=hf_token)
model.load_model(token=hf_token)
model.system_prompt = "You are good at SQL query"

app = FastAPI()

# Chat history storage
chat_history: Dict[str, List[Dict[str, str]]] = {}

# Request model for chat input
class ChatInput(BaseModel):
    session_id: str
    user_input: str

# Response model for chat output
class ChatResponse(BaseModel):
    response: str
    history: List[Dict[str, str]]

@app.post("/chat", response_model=ChatResponse)
async def chat(input: ChatInput):
    # Get session id and user input from the request
    session_id = input.session_id
    user_input = input.user_input

    # Initialize history if it doesn't exist
    if session_id not in chat_history:
        chat_history[session_id] = []

    # Add user input to the history
    history = chat_history[session_id]
    history.append({"role": "user", "content": user_input})

    # Prepare messages for the Llama3
    messages = [{"role": "system", "content": model.system_prompt}]
    messages.extend(history)

    # Get Llama3 response
    try:
        response = model.invoke(messages)
    except Exception as e:
        print('Llama3 invoke error')

    # Add assistant's response to the history
    history.append({"role": "assistant", "content": response})
    
    # Store updated history
    chat_history[session_id] = history

    return ChatResponse(response=response, history=history)
import os
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from schema.user_input import Response_output
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load .env
load_dotenv(override=True, dotenv_path=".env")

# CORS Middleware
def add_cors_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

# FastAPI App
app = FastAPI(
    description="FastAPI Demo",
    title="WebSocket API",
    version="1.0.0"
)
add_cors_middleware(app)

# Welcome route
@app.get(path="/hello", description="Simple greeting endpoint", response_model=Response_output)
def welcome():
    return {"message": "Welcome to the Gemini API!"}

# Gemini client
model = "gemini-2.0-flash-lite"
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# WebSocket endpoint
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()

    chat = client.aio.chats.create(
        model=model,
        config=types.GenerateContentConfig(
            system_instruction=[
                types.Part.from_text(text="You are a helpful assistant and will be answering user queries.")
            ],
            response_mime_type="text/plain",
        ),
        history=[]
    )

    try:
        while True:
            user_input = await websocket.receive_text()
            response_stream = await chat.send_message_stream(types.Part.from_text(text=f"""{user_input}"""))
            async for chunk in response_stream:
                if chunk.text:
                    await websocket.send_text(chunk.text)
                    await asyncio.sleep(0.5)
                    
    except WebSocketDisconnect:
        print("Client disconnected")

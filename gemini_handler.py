# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv(override=True, dotenv_path='.env')

async def generate():
    model = "gemini-2.0-flash-lite"
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    chat = client.aio.chats.create(
        model=model,
        config=types.GenerateContentConfig(
            system_instruction=[
                types.Part.from_text(text="""
        You are a helpful assistant and will be answering user queries.
        """),
            ],
            response_mime_type="text/plain",
        ),
        history=[]
    )
    while True:
        prompt = str(input("User >>> "))
        # Stream Gemini response
        response_stream = await chat.send_message_stream(types.Part.from_text(text=f"""{prompt}"""))
        async for chunk in response_stream:
            if chunk.text:
                print(chunk.text, end="")
                await asyncio.sleep(0.1)
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(generate())

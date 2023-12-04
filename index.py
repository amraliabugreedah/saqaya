import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2023-05-15"


response = openai.ChatCompletion.create(
    engine="opus-gpt4-32k",
    messages=[
        {
            "role": "system",
            "content": "You are a data analytics expert and you relate everything to soccer.",
        },
        {
            "role": "user",
            "content": "What's the most second needed thing in the world after oxygen?",
        },
        {
            "role": "assistant",
            "content": "I would say it's food or water.",
        },
        {"role": "user", "content": "Okay, what about the third one?"},
    ],
)

print(response)

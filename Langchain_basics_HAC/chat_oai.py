#import libraries

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

import os

# Validate API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")

model = ChatOpenAI(
    model="gpt-4o",
    max_tokens=500,
    api_key=api_key
)

# Make the prompt configurable
prompt = "Can you tell me about the latest advancements in GPU?"

try:
    result = model.invoke(prompt)
    print(result.content)
except Exception as e:
    print(f"An error occurred while calling the OpenAI API: {e}")


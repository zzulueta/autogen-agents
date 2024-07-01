# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("AZURE_OPENAI_KEY")
    return openai_api_key

def get_openai_api_model():
    load_env()
    openai_api_model = os.getenv("AZURE_OPENAI_MODEL")
    return openai_api_model

def get_openai_api_endpoint():
    load_env()
    openai_api_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    return openai_api_endpoint
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_face_config():
    endpoint = os.getenv("FACE_ENDPOINT")
    key = os.getenv("FACE_KEY")

    if not endpoint or not key:
        raise ValueError("FACE_ENDPOINT and FACE_KEY must be set in .env file")

    return endpoint, key

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
AI_FOUNDRY_AGENT_ID = os.getenv("AI_FOUNDRY_AGENT_ID")

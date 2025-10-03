# agents/summarizer.py

class Summarizer:
    def __init__(self, thread_client):
        self.thread_client = thread_client

    def run(self, prompt: str):
        return self.thread_client.run_agent(prompt)

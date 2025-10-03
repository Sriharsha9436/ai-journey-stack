from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import ListSortOrder, MessageRole
from config import PROJECT_ENDPOINT, AI_FOUNDRY_AGENT_ID

class ThreadClient:
    def __init__(self):
        if not PROJECT_ENDPOINT:
            raise ValueError("Please set PROJECT_ENDPOINT in your .env file")

        # Initialize the Azure AI Foundry client
        self.client = AgentsClient(
            endpoint=PROJECT_ENDPOINT,
            credential=DefaultAzureCredential()
        )

        # Set the agent ID
        self.agent_id = AI_FOUNDRY_AGENT_ID

        # Create a new thread for the conversation
        self.thread = self.client.threads.create()
        print(f"[ThreadClient] Created new thread: {self.thread.id}")

    def add_message(self, role: str, content: str):
        """
        Add a message to the thread (user or assistant)
        """
        self.client.messages.create(
            thread_id=self.thread.id,
            role=role,
            content=[{"type": "text", "text": content}]
        )
        print(f"[ThreadClient] Added {role} message: {content[:50]}...")

    def run_agent(self, prompt: str) -> str:
        """
        Send a user prompt to the agent, run the thread, and return the assistant response.
        """
        # Add the user message
        self.add_message("user", prompt)

        # Run the agent on the thread
        run = self.client.runs.create_and_process(
            thread_id=self.thread.id,
            agent_id=self.agent_id
        )

        # Check for failures
        if run.status == "failed":
            print(f"[ThreadClient] Run failed: {run.last_error}")
            return ""

        # Retrieve the last assistant message
        last_msg = self.client.messages.get_last_message_text_by_role(
            thread_id=self.thread.id,
            role=MessageRole.AGENT
        )
        if last_msg:
            print(f"[ThreadClient] Agent Response: {last_msg.text.value[:100]}...")
            return last_msg.text.value
        return ""

    def get_all_messages(self):
        """
        Retrieve all messages from the thread in chronological order
        """
        messages = self.client.messages.list(
            thread_id=self.thread.id,
            order=ListSortOrder.ASCENDING
        )
        return messages

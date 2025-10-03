from agents.summarizer import Summarizer
from agents.classifier import Classifier
from agents.recommender import Recommender
from utils.thread_client import ThreadClient

class SequentialOrchestrator:
    def __init__(self):
        # Initialize a single thread client for all agents
        self.thread_client = ThreadClient()

        # Initialize agents
        self.summarizer = Summarizer(self.thread_client)
        self.classifier = Classifier(self.thread_client)
        self.recommender = Recommender(self.thread_client)

    def run(self, user_input: str) -> dict:
        results = {}

        # Summarizer
        summary_prompt = f"Summarize the following text in 1-2 sentences:\n{user_input}"
        summary = self.summarizer.run(summary_prompt)
        results['summary'] = summary if summary else "No summary generated."

        # Classifier
        classifier_prompt = f"Classify the following input into one category: {user_input}"
        classification = self.classifier.run(classifier_prompt)
        results['classification'] = classification if classification else "No classification generated."

        # Recommender
        recommendation_prompt = f"The input was classified as '{classification}'. Give one actionable recommendation for the user or product team."
        recommendation = self.recommender.run(recommendation_prompt)
        results['recommendation'] = recommendation if recommendation else "No recommendation generated."

        return results

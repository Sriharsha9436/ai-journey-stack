from orchestration.sequential_orchestrator import SequentialOrchestrator

if __name__ == "__main__":
    orchestrator = SequentialOrchestrator()

    # Dynamic user input
    user_query = input("Enter your query: ")

    results = orchestrator.run(user_query)

    print("\n=== Orchestration Results ===")
    print(f"Summary: {results['summary']}")
    print(f"Classification: {results['classification']}")
    print(f"Recommendation: {results['recommendation']}")

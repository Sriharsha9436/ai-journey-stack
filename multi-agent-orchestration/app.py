import streamlit as st
from orchestration.sequential_orchestrator import SequentialOrchestrator

st.title("AI Multi-Agent Orchestration")

# Initialize orchestrator
orchestrator = SequentialOrchestrator()

# User input
user_query = st.text_area("Enter your query:")

if st.button("Run Orchestration") and user_query:
    # Run orchestrator
    results = orchestrator.run(user_query)

    # Display results
    st.subheader("Orchestration Results")
    st.markdown(f"**Summary:** {results['summary']}")
    st.markdown(f"**Classification:** {results['classification']}")
    st.markdown(f"**Recommendation:** {results['recommendation']}")

    # Display full thread logs
    st.subheader("Full Thread Logs")
    messages = orchestrator.thread_client.get_all_messages()
    for msg in messages:
        if msg.text_messages:
            last_msg = msg.text_messages[-1]
            st.text(f"{msg.role}: {last_msg.text.value}")

    # Save logs locally
    log_file = f"thread_{orchestrator.thread_client.thread.id}.txt"
    with open(log_file, "w", encoding="utf-8") as f:
        for msg in messages:
            if msg.text_messages:
                last_msg = msg.text_messages[-1]
                f.write(f"{msg.role}: {last_msg.text.value}\n")
    st.success(f"Thread logs saved to {log_file}")

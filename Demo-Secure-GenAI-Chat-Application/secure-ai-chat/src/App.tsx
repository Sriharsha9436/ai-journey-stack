import { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");

  async function sendPrompt(promptText: string) {
    try {
      const response = await fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: promptText })
      });

      const data = await response.json();
      console.log("✅ Response from backend:", data);
      setAnswer(data.answer?.chat_output || "No answer returned.");
    } catch (error) {
      console.error("❌ Error calling backend:", error);
      setAnswer("Something went wrong.");
    }
  }

  return (
    <div className="container">
      <h1>Secure AI Chat</h1>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={() => sendPrompt(prompt)}>Send</button>
      <div className="response">
        <h2>Answer:</h2>
        <p>{answer}</p>
      </div>
    </div>
  );
}

export default App;
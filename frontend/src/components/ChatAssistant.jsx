import { useState } from "react";
import API from "../services/api";

function ChatAssistant() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message) return;

    setLoading(true);

    try {
      const response = await API.post("/chat", {
  question: message,
});

      setAnswer(response.data.response);
    } catch (error) {
      console.error(error);
      setAnswer("Error communicating with AI Agent.");
    }

    setLoading(false);
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Ask Your AWS Account</h2>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Why is my AWS bill high?"
        style={{
          width: "70%",
          padding: "10px",
          marginRight: "10px",
        }}
      />

      <button onClick={sendMessage}>
        Ask Agent
      </button>

      {loading && <p>Thinking...</p>}

      {answer && (
        <div style={{ marginTop: "20px" }}>
          <h3>Agent Response</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default ChatAssistant;
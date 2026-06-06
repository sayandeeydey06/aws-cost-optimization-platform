import { useState } from "react";
import ReactMarkdown from "react-markdown";
import API from "../services/api";

function ChatAssistant() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

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

      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px",
        }}
      >
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Why is my AWS bill high?"
          style={{
            flex: 1,
            padding: "12px",
            borderRadius: "8px",
            border: "1px solid #ccc",
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button
          onClick={sendMessage}
          disabled={loading}
          style={{
            padding: "12px 20px",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          {loading ? "Thinking..." : "Ask Agent"}
        </button>
      </div>

      {answer && (
        <div
          style={{
            marginTop: "20px",
            padding: "20px",
            border: "1px solid #ddd",
            borderRadius: "12px",
            background: "#fafafa",
            textAlign: "left",
            lineHeight: "1.7",
          }}
        >
          <h3>Agent Response</h3>

          <ReactMarkdown>
            {answer}
          </ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default ChatAssistant;
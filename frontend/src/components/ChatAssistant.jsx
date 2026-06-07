import { useState } from "react";
import ReactMarkdown from "react-markdown";
import API from "../services/api";

function ChatAssistant() {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);

    try {
      const response = await API.post("/chat", {
        question: message,
      });

      setChatHistory((prev) => [
        ...prev,
        {
          question: message,
         answer: response.data.answer,
         tool: response.data.tool_used,
        },
      ]);

      setMessage("");
    } catch (error) {
      console.error(error);

      setChatHistory((prev) => [
        ...prev,
        {
          question: message,
          answer: "Error communicating with AI Agent.",
        },
      ]);
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
         {loading ? "Analyzing AWS..." : "Ask Agent"}
        </button>
      </div>

      <div style={{ marginTop: "20px" }}>
  {chatHistory.map((chat, index) => (
    <div key={index}>

      {/* User Message */}
      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          marginBottom: "10px",
        }}
      >
        <div
          style={{
            background: "#2563eb",
            color: "white",
            padding: "12px",
            borderRadius: "12px",
            maxWidth: "70%",
          }}
        >
          {chat.question}
        </div>
      </div>

      {/* AI Message */}
      <div
        style={{
          display: "flex",
          justifyContent: "flex-start",
          marginBottom: "20px",
        }}
      >
        <div
          style={{
            background: "#f3f4f6",
            padding: "12px",
            borderRadius: "12px",
            maxWidth: "80%",
            textAlign: "left",
          }}
        >
<div
  style={{
    fontSize: "12px",
    marginBottom: "10px",
    display: "inline-block",
    background: "#e0f2fe",
    padding: "4px 8px",
    borderRadius: "20px",
  }}
>
  Tool Used: {chat.tool}
</div>

<ReactMarkdown>
  {chat.answer}
</ReactMarkdown>
        </div>
      </div>

    </div>
  ))}
</div>
    </div>
  );
}

export default ChatAssistant;
import React from "react";

function ResponseCard({ response }) {
  return (
    <div className="response-card">
      <h2>🧠 AI Response</h2>
      <pre>{response}</pre>
    </div>
  );
}

export default ResponseCard;
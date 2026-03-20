import React, { useState } from "react";
import TriageForm from "./components/TriageForm";
import ResponseCard from "./components/ResponseCard";

function App() {
  const [response, setResponse] = useState("");

  return (
    <div className="container">
      <h1>🚑 AI Triage Assistant</h1>

      <TriageForm setResponse={setResponse} />

      {response && <ResponseCard response={response} />}
    </div>
  );
}

export default App;
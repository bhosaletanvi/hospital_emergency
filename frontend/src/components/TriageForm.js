import React, { useState } from "react";
import axios from "axios";

function TriageForm({ setResponse }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/triage", {
        query: query,
      });

      setResponse(res.data.response);
    } catch (err) {
      setResponse("❌ Error connecting to backend");
    }

    setLoading(false);
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <textarea
        placeholder="Enter patient symptoms..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        required
      />

      <button type="submit">
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </form>
  );
}

export default TriageForm;
🚑 Real-Time Emergency Response Triage Assistant
📌 Overview
AI-powered triage assistant that analyzes medical data and provides real-time emergency recommendations using Retrieval-Augmented Generation (RAG).

⚡ Features
Real-time response (<500ms goal)
Semantic search using FAISS
Noise reduction via context filtering
Basic triage prioritization (Red / Yellow / Green)
🛠 Tech Stack
Python
FastAPI
Sentence Transformers
FAISS
🚀 Run Locally
pip install -r requirements.txt
uvicorn backend.app:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import process_query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="🚑 Triage AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "Triage AI Agent is running 🚑"}


@app.post("/triage")
def triage(request: QueryRequest):
    result = process_query(request.query)
    return {"response": result}
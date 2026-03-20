from embeddings import create_index, search
from utils import clean_text

# Load dataset
def load_data():
    with open("backend/data/medical_data.txt", "r") as f:
        text = f.read()

    chunks = [clean_text(line) for line in text.split("\n") if line.strip()]
    return chunks


# Initialize index once (important for speed)
texts = load_data()
index, _ = create_index(texts)


def triage_logic(query: str):
    query_lower = query.lower()

    if "chest pain" in query_lower:
        return "🚨 HIGH PRIORITY (RED): Possible cardiac event. Perform ECG and give aspirin."
    elif "bleeding" in query_lower:
        return "🚨 HIGH PRIORITY (RED): Apply pressure immediately and control bleeding."
    elif "burn" in query_lower:
        return "🟡 MEDIUM PRIORITY: Cool burn under running water."
    else:
        return "🟢 LOW PRIORITY: Further diagnosis required."


def process_query(query: str):
    query = clean_text(query)

    # Retrieve relevant chunks
    relevant_chunks = search(query, index, texts)

    # Generate response
    response = "🔍 Relevant Medical Insights:\n"
    for chunk in relevant_chunks:
        response += f"- {chunk}\n"

    response += "\n" + triage_logic(query)

    return response
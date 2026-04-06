from fastapi import FastAPI, UploadFile
from app.ingestion.loader import load_ccda
from app.ingestion.chunker import chunk_text
from app.retrieval.vector_store import get_collection
from app.rag.pipeline import query_rag
import uuid

app = FastAPI()

sessions = {}

@app.post("/upload")
async def upload(file: UploadFile):
    content = await file.read()
    text = load_ccda(content.decode())

    chunks = chunk_text(text)

    session_id = str(uuid.uuid4())
    collection = get_collection(session_id)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[f"{i}"]
        )

    sessions["latest"] = session_id

    return {"session_id": session_id}

@app.get("/query")
def query(q: str):
    session_id = sessions.get("latest")
    answer, context = query_rag(session_id, q)
    return {"answer": answer, "context": context}
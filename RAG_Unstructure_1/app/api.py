from fastapi import FastAPI, UploadFile, File
import shutil
from app.rag_pipeline import ingest_document, query_rag

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_document(path)
    return {"message": "Document ingested"}


@app.get("/query")
def query(q: str):
    answer = query_rag(q)
    return {"answer": answer}

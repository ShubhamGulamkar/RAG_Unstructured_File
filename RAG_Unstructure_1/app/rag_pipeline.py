import chromadb
from app.config import settings
from app.embeddings import get_embedding
from app.data_loader import load_ccda, chunk_text
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

chroma_client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)
collection = chroma_client.get_or_create_collection(name="ccda_docs")


def ingest_document(file_path: str):
    text = load_ccda(file_path)
    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{file_path}_{i}"]
        )


def query_rag(question: str):
    query_embedding = get_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    context = "\n".join(results['documents'][0])

    prompt = f"""
    Answer the question based on context below:

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


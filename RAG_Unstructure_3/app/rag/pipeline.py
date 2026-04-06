from openai import OpenAI
from app.retrieval.vector_store import get_collection
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.hybrid_search import hybrid_search
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def query_rag(session_id, query):
    collection = get_collection(session_id)

    vector_results = collection.query(
        query_texts=[query],
        n_results=3
    )["documents"][0]

    bm25 = BM25Retriever(vector_results)
    bm25_results = bm25.search(query)

    context = hybrid_search(query, vector_results, bm25_results)

    prompt = f"""
    Context:
    {context}

    Question: {query}
    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, context
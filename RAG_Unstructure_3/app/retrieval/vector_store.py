import chromadb
from chromadb.utils import embedding_functions
from app.config import OPENAI_API_KEY, CHROMA_DB_DIR

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=OPENAI_API_KEY,
    model_name="text-embedding-3-small"
)

def get_collection(session_id):
    return client.get_or_create_collection(
        name=f"ccda_{session_id}",
        embedding_function=embedding_function
    )
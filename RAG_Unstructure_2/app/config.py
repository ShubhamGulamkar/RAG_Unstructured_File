import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./vectorstore")

settings = Settings()
from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self, documents):
        self.docs = documents
        self.tokenized = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized)

    def search(self, query, k=3):
        scores = self.bm25.get_scores(query.split())
        ranked = sorted(zip(self.docs, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in ranked[:k]]
def hybrid_search(query, vector_results, bm25_results):
    combined = list(set(vector_results + bm25_results))
    return combined[:5]
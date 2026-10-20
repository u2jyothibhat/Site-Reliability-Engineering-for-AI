EMBEDDING_MODEL = "text-embed-v3"

def retrieve(query: str, user, k: int = 8):
    query_vector = embed(query, model=EMBEDDING_MODEL)
    filters = {
        "embedding_model": EMBEDDING_MODEL,
        "status": "active",
        "allowed_groups": {"any_of": user.groups},
    }
    results = vector_client.search(
        index="policy-docs",
        vector=query_vector,
        top_k=k,
        filter=filters,
    )
    metrics.histogram("retrieval_top_score", results[0].score if results else 0)
    metrics.counter("retrieval_empty_total", 1 if not results else 0)
    return results

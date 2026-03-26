"""
Retrieval module

This module selects the most relevant text chunks for a user query.
In a full RAG system, retrieval would use similarity search over
embedding vectors.
"""

from typing import List


def retrieve_top_chunks(query: str, chunks: List[str], top_k: int = 3) -> List[str]:
    """
    Retrieve the most relevant chunks for a query.

    Parameters
    ----------
    query : str
        User question
    chunks : List[str]
        Available text chunks
    top_k : int
        Number of chunks to return

    Returns
    -------
    List[str]
        Top matching chunks
    """

    query_words = query.lower().split()
    scored_chunks = []

    for chunk in chunks:
        score = sum(word in chunk.lower() for word in query_words)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda item: item[0])

    top_chunks = [chunk for _, chunk in scored_chunks[:top_k]]

    print(f"Retrieved {len(top_chunks)} chunks for query: {query}")
    return top_chunks

"""
RAG pipeline module

This module connects document loading, simple embedding generation,
and retrieval into one workflow.
"""

from ingestion import load_documents
from embedding import generate_embeddings
from retrieval import retrieve_top_chunks


def split_into_chunks(documents, chunk_size=200):
    """
    Split documents into smaller chunks.

    Parameters
    ----------
    documents : list
        List of document texts
    chunk_size : int
        Approximate size of each chunk

    Returns
    -------
    list
        List of text chunks
    """

    chunks = []

    for document in documents:
        for i in range(0, len(document), chunk_size):
            chunks.append(document[i:i + chunk_size])

    return chunks


def run_rag_pipeline(folder_path, query):
    """
    Run a basic RAG-style workflow.

    Parameters
    ----------
    folder_path : str
        Folder containing source documents
    query : str
        User question

    Returns
    -------
    list
        Retrieved chunks relevant to the query
    """

    documents = load_documents(folder_path)
    chunks = split_into_chunks(documents)
    _ = generate_embeddings(chunks)
    top_chunks = retrieve_top_chunks(query, chunks)

    return top_chunks

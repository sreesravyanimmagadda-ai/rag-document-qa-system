"""
Simple application entry point for the RAG system.
"""

from src.rag_pipeline import run_rag_pipeline


def main():
    """
    Example usage of the RAG pipeline.
    """

    document_folder = "data"
    query = "What information is contained in the documents?"

    results = run_rag_pipeline(document_folder, query)

    print("\nRetrieved Chunks:\n")

    for chunk in results:
        print("-" * 40)
        print(chunk)


if __name__ == "__main__":
    main()

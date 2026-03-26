"""
Document ingestion module

This module loads documents from a folder so they can be used
by the RAG pipeline.
"""

import os


def load_documents(folder_path):
    """
    Load .txt documents from a directory.

    Parameters
    ----------
    folder_path : str
        Path to the document folder

    Returns
    -------
    list
        List of document contents
    """

    documents = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            full_path = os.path.join(folder_path, file_name)

            with open(full_path, "r", encoding="utf-8") as file:
                documents.append(file.read())

    print(f"Loaded {len(documents)} documents from {folder_path}")
    return documents

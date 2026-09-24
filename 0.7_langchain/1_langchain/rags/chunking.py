import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"BASE_DIR:{BASE_DIR}")

def load_folder(folder_path: str):
    documents = []
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            documents.extend(PyPDFLoader(path).load())
        elif filename.endswith(".txt"):
            documents.extended(TextLoader(path).load)
    return documents
docs = load_folder(os.path.join(BASE_DIR, "docs"))
print(f"Step1 - loaded{len(docs)} raw documents")

print("PRINTING DOCUMENTS....................")

splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunk=splitter.split_documents(docs)
print(f"stage 2 split: {len(chunk)} chunk")
print(f"preview of chunk 0: {chunk[0].page_content}...")
print(f"Preview of chunk 1: {chunk[1].page_content}....")
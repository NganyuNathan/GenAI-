from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

docs = PyPDFLoader("docs/Workbook.pdf").load()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
query = "What is Revised German Spelling Conventions"

for chunk_size in [300, 800, 1500]:
    overlap = int(chunk_size * 0.15)
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_documents(docs)

    len_content = [len(c.page_content) for c in chunks]
    average_length = sum(len_content) / len(len_content)

    store = InMemoryVectorStore(embeddings)
    store.add_documents(chunks)

    top_result = store.similarity_search(query, k=1)[0]

    print(f"\n=== Chunk size {chunk_size} (overlap {overlap}) ===")
    print(f"Total chunks: {len(chunks)}")
    print(f"Average chunk length: {average_length:.0f} characters")
    print(f"Top match for: '{query}':\n{top_result.page_content[:200]}...")
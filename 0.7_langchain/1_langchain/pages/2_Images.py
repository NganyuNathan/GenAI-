
from core.ingestion import load_documents, load_spliit_folder
import streamlit as st

files = st.file_uploader(
    "Upload documents", type=["pdf", "txt"], accept_multiple_files=True
)
model = load_spliit_folder()
result = model.invoke(files)
# import streamlit as st
# import requests

# API_URL = "http://localhost:8000"

# st.title("CCDA RAG System")

# uploaded_file = st.file_uploader("Upload CCDA XML", type=["xml"])

# if uploaded_file:
#     files = {"file": uploaded_file.getvalue()}
#     res = requests.post(f"{API_URL}/upload", files={"file": uploaded_file})
#     st.success("Uploaded and indexed!")

# query = st.text_input("Ask a question")

# if st.button("Search"):
#     res = requests.get(f"{API_URL}/query", params={"q": query})
#     st.write(res.json()["answer"])

import streamlit as st
import requests
import hashlib

API_URL = "http://localhost:8000"

st.title("Healthcare RAG (CCDA)")

# Prevent duplicate uploads using session state
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = set()

file = st.file_uploader("Upload CCDA", type=["xml"])

if file:
    file_bytes = file.getvalue()
    file_hash = hashlib.md5(file_bytes).hexdigest()

    if file_hash not in st.session_state.uploaded_files:
        files = {"file": (file.name, file_bytes, "application/xml")}
        response = requests.post(f"{API_URL}/upload", files=files)

        if response.status_code == 200:
            st.success("Uploaded and indexed successfully!")
            st.session_state.uploaded_files.add(file_hash)
        else:
            st.error("Upload failed")
    else:
        st.info("File already uploaded. Skipping duplicate upload.")

q = st.text_input("Ask clinical question")

if st.button("Ask"):
    res = requests.get(f"{API_URL}/query", params={"q": q})
    st.write(res.json()["answer"])
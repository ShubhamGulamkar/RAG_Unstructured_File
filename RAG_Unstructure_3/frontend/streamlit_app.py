# import streamlit as st
# import requests

# st.title("CCDA RAG System")

# file = st.file_uploader("Upload CCDA")

# if file:
#     res = requests.post("http://localhost:8000/upload", files={"file": file})
#     st.success("Uploaded!")

# query = st.text_input("Ask a question")

# if st.button("Ask"):
#     res = requests.get("http://localhost:8000/query", params={"q": query})
#     st.write(res.json())

import streamlit as st
import requests

st.title("CCDA RAG System")

# Initialize session state
if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

file = st.file_uploader("Upload CCDA")

# Upload ONLY ONCE
if file and not st.session_state.uploaded:
    res = requests.post(
        "http://localhost:8000/upload",
        files={"file": file.getvalue()}
    )
    st.session_state.uploaded = True
    st.success("Uploaded!")

query = st.text_input("Ask a question")

if st.button("Ask"):
    res = requests.get(
        "http://localhost:8000/query",
        params={"q": query}
    )
    st.write(res.json())
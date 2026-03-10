import streamlit as st
import requests

API_URL = "http://rag-api:8000"

st.title("AI Document Intelligence")

st.subheader("Upload PDF")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    files = {"file": uploaded_file}
    response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        st.success("PDF uploaded successfully")
    else:
        st.error("Upload failed")


st.subheader("Ask a Question")

question = st.text_input("Enter your question")

if st.button("Ask"):
    response = requests.post(
        f"{API_URL}/query",
        json={"question": question},
        timeout=30
    )

    if response.status_code == 200:
        data = response.json()

        st.subheader("Answer")
        answer = data.get("answer", "No answer returned")
        if answer:
            st.write(answer)
        else:
            st.write("No answer returned — check that PDF was uploaded and vector store is populated.")

        st.subheader("Retrieved Context")
        for chunk in data.get("retrieved_chunks", []):
            st.write(f"- {chunk}")
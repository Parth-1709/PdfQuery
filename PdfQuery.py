import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import streamlit as st

st.set_page_config(
    page_title="PDF Q&A",
    page_icon="📄"
)

st.title("📄 Chat with your PDF")
st.write("Upload a PDF and ask questions about its contents.")

file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if file:
    with open("temp.pdf", "wb") as f:
        f.write(file.getbuffer())

    loader = PyPDFLoader('temp.pdf')
    doc = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=50)
    new_doc = splitter.split_documents(doc)

    embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

    db = FAISS.from_documents(new_doc,embedding)
    retriever = db.as_retriever()

    llm = ChatGroq(model='openai/gpt-oss-120b')

    prompt = ChatPromptTemplate.from_messages(
        [
            ('system','''
                    Answer the following question in 1-2 sentences based on the context provided only.if there is no context return that the question is irrelevant.
                    Context:{context}
            '''),
            ('user','{question}')
        ]
    )



    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            'context':retriever|format_docs,
            'question':RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    question = st.text_input(
            "Ask a question about your PDF:"
        )

    if st.button("Ask"):

        if question.strip():

            with st.spinner("Thinking..."):

                answer = chain.invoke(question)

            st.subheader('Answer')
            st.write(answer)

        else:

            st.warning("Please enter a question.")



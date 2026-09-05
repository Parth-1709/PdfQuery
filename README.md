# 📄 AI PDF Q&A

An AI-powered **PDF Question & Answer application** built using **Streamlit, LangChain, Hugging Face embeddings, FAISS, and Groq**.

The application allows users to upload a PDF and ask questions about its contents. It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the document before generating an answer.

## 🚀 Live Demo

🔗 **[PDF Q&A · Streamlit](https://pdfquery-parth.streamlit.app/)**

Upload a PDF and start asking questions about it.

## ✨ Features

* 📄 Upload PDF documents
* 🔍 Retrieve relevant information from the uploaded document
* 🤖 Generate answers using an LLM
* 🧠 Uses Retrieval-Augmented Generation (RAG)
* 🚫 Avoids answering questions when the required information is not available in the PDF
* ⚡ Fast LLM inference using Groq
* 🖥️ Interactive Streamlit interface
* 🔢 Vector similarity search using FAISS
* 🧩 Hugging Face embeddings for semantic search

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — Web application interface
* **LangChain** — RAG pipeline and LLM orchestration
* **Groq** — LLM inference
* **Hugging Face** — Text embeddings
* **FAISS** — Vector similarity search
* **PyMuPDF** — PDF text extraction

## 🏗️ Architecture

```text
                         User
                          │
                          ▼
                    Upload PDF
                          │
                          ▼
                     PyMuPDF
                          │
                          ▼
                    Extract Text
                          │
                          ▼
                    Text Chunking
                          │
                          ▼
               Hugging Face Embeddings
                          │
                          ▼
                       FAISS
                   Vector Database
                          │
                          │
                    User Question
                          │
                          ▼
                      Retriever
                          │
                          ▼
                Relevant PDF Chunks
                          │
                          ▼
               ChatPromptTemplate
                  ┌───────┴───────┐
                  │               │
               Context         Question
                  │               │
                  └───────┬───────┘
                          ▼
                       ChatGroq
                          │
                          ▼
                  StrOutputParser
                          │
                          ▼
                       Answer
```

## 🔄 RAG Pipeline

The application follows a Retrieval-Augmented Generation workflow.

### 1. PDF Upload

The user uploads a PDF through the Streamlit interface.

### 2. Text Extraction

**PyMuPDF** extracts the text and metadata from the PDF.

### 3. Text Chunking

The extracted text is divided into smaller chunks using a text splitter.

This makes it possible to retrieve specific sections of the document rather than passing the entire PDF to the LLM.

### 4. Embeddings

Each chunk is converted into a numerical vector using a **Hugging Face embedding model**.

These vectors represent the semantic meaning of the text.

### 5. Vector Store

The embeddings are stored in **FAISS**, which allows efficient similarity search.

### 6. Retrieval

When the user asks a question, the question is converted into an embedding and the retriever searches FAISS for the most relevant document chunks.

### 7. Prompt Construction

The retrieved chunks are provided as context to the LLM along with the user's question.

### 8. LLM Generation

**Groq** is used to run the language model and generate an answer based on the retrieved context.

### 9. Output Parsing

`StrOutputParser` converts the LLM response into a plain string that can be displayed in the Streamlit interface.

## 🔗 LangChain Chain

The core RAG chain follows this structure:

```python
chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)
```

The flow can be summarized as:

```text
Question
   │
   ├──────────────► Retriever ──────► Context
   │
   └──────────────► RunnablePassthrough ──► Question
                                      │
                                      ▼
                              Prompt Template
                                      │
                                      ▼
                                    LLM
                                      │
                                      ▼
                              Output Parser
                                      │
                                      ▼
                                   Answer
```

## 🧠 Handling Irrelevant Questions

The application instructs the LLM to answer **only using information provided in the retrieved PDF context**.

If the retrieved context does not contain enough information to answer the question, the application responds that the information is not available in the uploaded PDF instead of relying on the model's general knowledge.

This helps reduce unsupported or hallucinated answers.

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 API Key Setup

The application uses a **Groq API key**.

For local development, create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

The application loads the environment variable using `python-dotenv`.

**Never commit your `.env` file or API key to GitHub.**

Add the following to `.gitignore`:

```text
.env
.streamlit/secrets.toml
```

### Streamlit Deployment

For deployment, add the API key through Streamlit's Secrets configuration:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

LangChain's `ChatGroq` can automatically retrieve the `GROQ_API_KEY` environment variable.

## ▶️ Run Locally

Run the application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> `.env` is only used for local development and should not be committed to the repository.

## 📋 Requirements

The main dependencies used by the application are:

```text
streamlit
python-dotenv
langchain
langchain-groq
langchain-community
langchain-huggingface
langchain-text-splitters
sentence-transformers
faiss-cpu
pymupdf
```

See `requirements.txt` for the complete dependency list.

## 🔮 Future Improvements

Potential improvements include:

* 💬 Add conversational chat history
* 📚 Support multiple PDFs
* 🔎 Display the source pages used for each answer
* 📌 Highlight the relevant sections of the PDF
* 🧠 Improve retrieval with hybrid search
* ⚡ Add streaming responses
* 💾 Add persistent vector database storage
* 🎤 Add voice-based questions
* 📥 Allow users to download generated answers

## 🎯 Learning Objectives

This project was built to gain practical experience with:

* Generative AI
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Embeddings
* Vector databases
* Semantic similarity search
* Document chunking
* Retrieval pipelines
* LangChain LCEL
* Prompt engineering
* Output parsing
* API-based LLM inference
* Streamlit application development
* AI application deployment

## 📄 License

This project is intended for learning, experimentation, and portfolio purposes.

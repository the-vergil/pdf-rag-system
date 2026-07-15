# 📄 PDF RAG System

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents, store their semantic embeddings in a vector database, and ask natural language questions about the uploaded content.

The system extracts text from PDFs, chunks the content, generates embeddings using Google's Gemini Embedding Model, stores vectors in Qdrant, retrieves relevant context based on user queries, and generates context-aware answers using Gemini 2.5 Flash.

---

## 🚀 Features

* Upload and process PDF documents
* Automatic text extraction and chunking
* Semantic embeddings using Gemini Embeddings
* Vector storage using Qdrant
* Context retrieval with similarity search
* Question-answering powered by Gemini 2.5 Flash
* Event-driven workflow orchestration using Inngest
* Interactive Streamlit interface
* FastAPI backend integration

---

## 🏗️ Architecture

```text
                ┌─────────────┐
                │   PDF File  │
                └──────┬──────┘
                       │
                       ▼
            ┌────────────────────┐
            │ PDF Text Extraction│
            └─────────┬──────────┘
                      │
                      ▼
            ┌───────────────────┐
            │ Text Chunking     │
            └─────────┬─────────┘
                      │
                      ▼
            ┌───────────────────┐
            │ Gemini Embeddings │
            └─────────┬─────────┘
                      │
                      ▼
            ┌───────────────────┐
            │ Qdrant Vector DB  │
            └─────────┬─────────┘
                      │
      User Query      │
           │          │
           ▼          ▼
    ┌───────────────────────┐
    │ Similarity Retrieval  │
    └──────────┬────────────┘
               │
               ▼
    ┌───────────────────────┐
    │ Gemini 2.5 Flash LLM  │
    └──────────┬────────────┘
               │
               ▼
         Generated Answer
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Inngest

### LLM & Embeddings

* Gemini 2.5 Flash
* Gemini Embedding 001

### Vector Database

* Qdrant

### Frontend

* Streamlit

### Document Processing

* LlamaIndex
* PDFReader
* SentenceSplitter

---

## 📂 Project Structure

```text
PDF-RAG-System/
│
├── main.py                # FastAPI + Inngest functions
├── data_loader.py         # PDF loading and embeddings
├── vector_db.py           # Qdrant operations
├── custom_types.py        # Pydantic models
├── streamlit_app.py       # Streamlit UI
├── uploads/               # Uploaded PDFs
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

### PDF Ingestion

1. User uploads a PDF.
2. PDF text is extracted.
3. Content is split into chunks.
4. Gemini generates embeddings.
5. Embeddings are stored in Qdrant.

### Question Answering

1. User asks a question.
2. Question is converted into an embedding.
3. Qdrant retrieves the most relevant chunks.
4. Retrieved chunks are passed to Gemini 2.5 Flash.
5. Gemini generates an answer using only the retrieved context.


## 🐳 Start Qdrant

Run Qdrant using Docker:

```bash
docker run -d \
--name qdrantRagDb \
-p 6333:6333 \
-v "$(pwd)/qdrant_storage:/qdrant/storage" \
qdrant/qdrant
```

Verify Qdrant:

```bash
http://localhost:6333/dashboard
```

---

## ▶️ Running the Application

### Start FastAPI + Inngest

```bash
uvicorn main:app --reload
```

Default:

```text
http://127.0.0.1:8000
```

---

### Start Streamlit

```bash
streamlit run streamlit_app.py
```

Default:

```text
http://localhost:8501
```

---

## 📖 Usage

### Upload PDF

* Open Streamlit UI.
* Upload a PDF document.
* Wait for ingestion to complete.

### Ask Questions

Example queries:

```text
What is the main objective of this document?

Summarize the key findings.

What technologies are discussed?

Who are the stakeholders mentioned?

Explain the methodology section.
```

---

## 📌 Example RAG Flow

### Query

```text
What is Retrieval-Augmented Generation?
```

### Retrieved Context

```text
RAG combines information retrieval with large language models.
```

### Generated Response

```text
Retrieval-Augmented Generation (RAG) is a technique that combines a retrieval system with a language model to generate responses grounded in external knowledge.
```

---

## 🔍 API Events

### PDF Ingestion Event

```json
{
  "name": "rag/ingest-pdf",
  "data": {
    "pdf_path": "/path/to/file.pdf",
    "source_id": "file.pdf"
  }
}
```

### Query Event

```json
{
  "name": "rag/query_pdf_ai",
  "data": {
    "question": "What is RAG?",
    "top_k": 5
  }
}
```


## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added feature"
```

4. Push branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Chet Mani Singh**

If you found this project useful, consider giving it a ⭐ on GitHub.

<div align="center">

# 🤖 AI RAG Chatbot

**Chat with your own documents — powered by Retrieval-Augmented Generation**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-6E56CF)](https://www.trychroma.com/)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-LLM-4285F4?logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

</div>

---

## 📖 Overview

**AI RAG Chatbot** is a Retrieval-Augmented Generation (RAG) application that lets you upload a document — PDF, DOCX, TXT, CSV, or XLSX — and have a natural conversation with it. Instead of relying purely on an LLM's built-in knowledge, the app retrieves the most relevant passages from *your* document and feeds them to the model as grounded context, producing answers that are accurate, source-based, and free of hallucinated facts wherever possible.

The project has two entry points:

- **`main.py`** — a lightweight command-line demo that loads a sample PDF (`data/Ai_Research.pdf`) and answers a single question.
- **`app.py`** — a full **Streamlit** web app with document upload, a styled chat interface, and session-based conversation history.

---

## ✨ Features

- 📄 **Multi-format ingestion** — PDF, DOCX, TXT, CSV, and XLSX supported out of the box
- ✂️ **Smart chunking** — recursive character-based text splitting with overlap to preserve context
- 🧠 **Semantic embeddings** — Hugging Face `sentence-transformers/all-MiniLM-L6-v2`
- 🗂️ **Persistent vector storage** — documents are embedded and stored in a local **ChromaDB** instance
- 🔍 **Top-k semantic retrieval** — pulls the most relevant chunks for every query
- 💬 **Grounded generation** — **Google Gemini** answers strictly from retrieved context
- 🖥️ **Polished chat UI** — dark-themed Streamlit interface with chat bubbles, avatars, and status indicators
- ⚡ **Simple, modular codebase** — each RAG stage lives in its own file under `src/`

---

## 🧭 Workflow Diagram

The diagram below shows the end-to-end pipeline — from document upload to a grounded chatbot answer.

```mermaid
flowchart TD
    A[📄 User uploads document<br/>PDF / DOCX / TXT / CSV / XLSX] --> B["document_loader.py<br/>load_document()"]
    B --> C["chunking.py<br/>split_documents()<br/>RecursiveCharacterTextSplitter (500 / 50)"]
    C --> D["embeddings.py<br/>create_embeddings()<br/>HuggingFace all-MiniLM-L6-v2"]
    D --> E["vector_store.py<br/>create_vector_db()<br/>ChromaDB (persist_directory)"]
    E --> F["retriever.py<br/>get_retriever()<br/>top-k = 3 similarity search"]
    F --> G["llm.py<br/>create_llm()<br/>Google Gemini"]
    G -.stored in session state.-> H((Ready to Chat))

    H --> I[🙋 User asks a question]
    I --> J["chatbot.py → get_answer()<br/>retriever.invoke(question)"]
    J --> K[Relevant chunks retrieved<br/>from ChromaDB]
    K --> L[Context + question<br/>combined into prompt]
    L --> M["llm.invoke(prompt)<br/>Gemini generates answer"]
    M --> N[💬 Answer rendered<br/>in Streamlit chat bubble]
    N --> I

    style A fill:#2563eb,color:#fff
    style H fill:#22c55e,color:#000
    style M fill:#0ea5e9,color:#fff
    style N fill:#6366f1,color:#fff
```

**Pipeline stages explained:**

| Stage | Module | Responsibility |
|---|---|---|
| 1. Load | `src/document_loader.py` | Detects file type and loads it via the matching LangChain loader (`PyPDFLoader`, `Docx2txtLoader`, `TextLoader`, `CSVLoader`, `UnstructuredExcelLoader`) |
| 2. Chunk | `src/chunking.py` | Splits documents into overlapping 500-character chunks for better retrieval granularity |
| 3. Embed | `src/embeddings.py` | Converts chunks into dense vector embeddings using a Hugging Face sentence-transformer |
| 4. Store | `src/vector_store.py` | Persists embeddings in a local ChromaDB collection |
| 5. Retrieve | `src/retriever.py` | Fetches the top-3 most semantically similar chunks for a given question |
| 6. Generate | `src/llm.py` + `src/chatbot.py` | Builds a context-grounded prompt and calls Gemini to produce the final answer |

---

## 🔄 State Diagram

This state diagram models the chatbot session's lifecycle inside the Streamlit app (`app.py`).

```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle: 🌀 Idle\n(no document processed)
    Idle --> Uploading: user selects a file

    Uploading: 📤 Uploading\nfile saved to temp path
    Uploading --> Processing: "Process Document" clicked

    Processing: ⚙️ Processing\nload → chunk → embed → store → retriever → LLM
    Processing --> Ready: pipeline succeeds
    Processing --> Error: exception raised

    Error: ❌ Error\nshow st.error(message)
    Error --> Idle: user retries upload

    Ready: 🟢 Ready\nretriever & LLM cached in session_state
    Ready --> AwaitingQuestion: chat input displayed

    AwaitingQuestion: ⌨️ Awaiting Question
    AwaitingQuestion --> Thinking: user submits question
    AwaitingQuestion --> Uploading: user uploads a new document

    Thinking: 🤔 Thinking\nretrieve context + call Gemini
    Thinking --> Answered: response generated

    Answered: 💬 Answered\nmessage appended to chat history
    Answered --> AwaitingQuestion: st.rerun()

    Ready --> [*]
```

---

## 🖼️ Output Screenshots

Screenshots of the running Streamlit application are available in the [`Streamlit Screenshots/`](./Streamlit%20Screenshots) folder of this repository.

<div align="center">

**Home screen — before any document is uploaded**

<img src="./Streamlit%20Screenshots/RAG%20streamlit1.png" alt="AI RAG Chatbot - initial screen" width="700"/>

**Document uploaded and processed**

<img src="./Streamlit%20Screenshots/RAG%20streamlit%202.png" alt="AI RAG Chatbot - document processed" width="700"/>

**Conversation in progress**

<img src="./Streamlit%20Screenshots/RAG%20streamlit%203.png" alt="AI RAG Chatbot - chat conversation" width="700"/>

**Grounded answer returned from the document**

<img src="./Streamlit%20Screenshots/RAG%20streamlit%204.png" alt="AI RAG Chatbot - answer generated" width="700"/>

**Extended chat history view**

<img src="./Streamlit%20Screenshots/RAG%20streamlit%205.png" alt="AI RAG Chatbot - chat history" width="700"/>

</div>

> 💡 If the images don't render, make sure the `Streamlit Screenshots` folder (with that exact name, including the space) stays at the root of the repository, alongside this `README.md`.

---

## 🗂️ Project Structure

```
AI_RAG-CHATBOT/
├── app.py                     # Streamlit web application (chat UI)
├── main.py                    # CLI demo — single-question RAG example
├── requirements.txt           # Python dependencies
├── .gitignore
├── data/
│   └── Ai_Research.pdf        # Sample document used by main.py
├── src/
│   ├── document_loader.py     # Multi-format document loading
│   ├── chunking.py            # Text splitting into chunks
│   ├── embeddings.py          # Hugging Face embedding model
│   ├── vector_store.py        # ChromaDB vector store creation
│   ├── retriever.py           # Top-k retriever
│   ├── llm.py                 # Gemini LLM initialization
│   ├── prompts.py             # RAG prompt template
│   ├── chatbot.py             # Retrieval + generation orchestration
│   └── memory.py              # In-memory chat history helper
└── Streamlit Screenshots/     # UI output screenshots
    ├── RAG streamlit1.png
    ├── RAG streamlit 2.png
    ├── RAG streamlit 3.png
    ├── RAG streamlit 4.png
    └── RAG streamlit 5.png
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangChain |
| Embeddings | Hugging Face `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Database | ChromaDB |
| LLM | Google Gemini (`langchain-google-genai`) |
| Document Parsing | `pypdf`, `python-docx`, `pandas`, `openpyxl`, `unstructured` |
| Language | Python 3.10+ |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Omajamshed/AI_RAG-CHATBOT.git
cd AI_RAG-CHATBOT
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> ⚠️ **Security note:** `src/llm.py` currently references the API key directly in code. For any real or shared deployment, load it from the environment instead, e.g.:
> ```python
> import os
> from dotenv import load_dotenv
> load_dotenv()
> llm = ChatGoogleGenerativeAI(
>     model="gemini-3.6-flash",
>     google_api_key=os.getenv("GOOGLE_API_KEY")
> )
> ```
> Never commit real API keys to version control.

---

## ▶️ Usage

### Run the Streamlit app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`), upload a document, click **Process Document**, and start chatting.

### Run the CLI demo

```bash
python main.py
```

This loads the bundled `data/Ai_Research.pdf`, prompts you for a question in the terminal, and prints the generated answer.

---

## 🔮 Roadmap

- [ ] Move the Gemini API key to environment variables (`.env`) across the codebase
- [ ] Add conversational memory so follow-up questions retain prior context
- [ ] Support multi-document upload and cross-document retrieval
- [ ] Add source citations (page/section) alongside generated answers
- [ ] Deploy a hosted demo (Streamlit Community Cloud / Hugging Face Spaces)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, new loaders, UI improvements, or additional LLM/embedding backends.

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

Built with ❤️ using LangChain, ChromaDB, Hugging Face, and Google Gemini.

</div>

# import streamlit as st
# import tempfile
# import os
#
# from src.document_loader import load_document
# from src.chunking import split_documents
# from src.embeddings import create_embeddings
# from src.vector_store import create_vector_db
# from src.retriever import get_retriever
# from src.llm import create_llm
# from src.chatbot import get_answer
#
#
# # -----------------------------
# # Page Settings
# # -----------------------------
#
# st.set_page_config(
#     page_title="AI RAG Chatbot",
#     page_icon="🤖",
#     layout="centered"
# )
#
#
# # -----------------------------
# # CSS - Chat Style UI
# # -----------------------------
#
# st.markdown("""
# <style>
#
# .main {
#     background-color: #0e1117;
# }
#
# .title {
#     text-align: center;
#     font-size: 32px;
#     font-weight: bold;
#     margin-bottom: 5px;
# }
#
# .subtitle {
#     text-align: center;
#     color: #9ca3af;
#     margin-bottom: 25px;
# }
#
# .upload-box {
#     padding: 20px;
#     border-radius: 15px;
#     background-color: #171b24;
#     border: 1px solid #303641;
#     margin-bottom: 20px;
# }
#
# .user-message {
#     background-color: #2563eb;
#     color: white;
#     padding: 12px 18px;
#     border-radius: 15px 15px 4px 15px;
#     margin: 10px 0 10px auto;
#     max-width: 75%;
# }
#
# .ai-message {
#     background-color: #202631;
#     color: white;
#     padding: 12px 18px;
#     border-radius: 15px 15px 15px 4px;
#     margin: 10px auto 10px 0;
#     max-width: 75%;
# }
#
# </style>
# """, unsafe_allow_html=True)
#
#
# # -----------------------------
# # Title
# # -----------------------------
#
# st.markdown(
#     '<div class="title">🤖 AI RAG Chatbot</div>',
#     unsafe_allow_html=True
# )
#
# st.markdown(
#     '<div class="subtitle">Upload a document and ask questions about it</div>',
#     unsafe_allow_html=True
# )
#
#
# # -----------------------------
# # Session State
# # -----------------------------
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# if "retriever" not in st.session_state:
#     st.session_state.retriever = None
#
# if "llm" not in st.session_state:
#     st.session_state.llm = None
#
#
# # -----------------------------
# # Document Upload
# # -----------------------------
#
# st.markdown(
#     '<div class="upload-box">',
#     unsafe_allow_html=True
# )
#
# st.subheader("📄 Upload Document")
#
# uploaded_file = st.file_uploader(
#     "Choose a file",
#     type=["pdf", "docx", "txt", "csv", "xlsx"]
# )
#
# if uploaded_file:
#
#     st.write(
#         f"📎 **{uploaded_file.name}**"
#     )
#
#     process_button = st.button(
#         "⚙️ Process Document",
#         use_container_width=True
#     )
#
#     if process_button:
#
#         with st.spinner("Processing document..."):
#
#             try:
#
#                 # Save uploaded file temporarily
#                 file_extension = os.path.splitext(
#                     uploaded_file.name
#                 )[1]
#
#                 with tempfile.NamedTemporaryFile(
#                     delete=False,
#                     suffix=file_extension
#                 ) as temp_file:
#
#                     temp_file.write(
#                         uploaded_file.getbuffer()
#                     )
#
#                     file_path = temp_file.name
#
#
#                 # 1. Load document
#                 documents = load_document(
#                     file_path
#                 )
#
#
#                 # 2. Chunk document
#                 chunks = split_documents(
#                     documents
#                 )
#
#
#                 # 3. Create embeddings
#                 embeddings = create_embeddings()
#
#
#                 # 4. Create vector store
#                 vector_store = create_vector_db(
#                     chunks,
#                     embeddings
#                 )
#
#
#                 # 5. Create retriever
#                 retriever = get_retriever(
#                     vector_store
#                 )
#
#
#                 # 6. Create LLM
#                 llm = create_llm()
#
#
#                 # Save for chat
#                 st.session_state.retriever = retriever
#                 st.session_state.llm = llm
#
#
#                 # Delete temporary file
#                 os.remove(file_path)
#
#
#                 st.success(
#                     "✅ Document processed successfully!"
#                 )
#
#             except Exception as e:
#
#                 st.error(
#                     f"Error: {e}"
#                 )
#
# st.markdown(
#     '</div>',
#     unsafe_allow_html=True
# )
#
#
# # -----------------------------
# # Chat History
# # -----------------------------
#
# for message in st.session_state.messages:
#
#     if message["role"] == "user":
#
#         st.markdown(
#             f"""
#             <div class="user-message">
#                 <b>You</b><br>
#                 {message["content"]}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#
#     else:
#
#         st.markdown(
#             f"""
#             <div class="ai-message">
#                 <b>🤖 AI Assistant</b><br>
#                 {message["content"]}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#
#
# # -----------------------------
# # Chat Input
# # -----------------------------
#
# question = st.chat_input(
#     "Ask something about your document..."
# )
#
#
# if question:
#
#     # Check document
#     if st.session_state.retriever is None:
#
#         st.warning(
#             "Please upload and process a document first."
#         )
#
#     else:
#
#         # Show user question
#         st.session_state.messages.append(
#             {
#                 "role": "user",
#                 "content": question
#             }
#         )
#
#
#         # Get answer from RAG
#         with st.spinner("Thinking..."):
#
#             answer = get_answer(
#                 question,
#                 st.session_state.retriever,
#                 st.session_state.llm
#             )
#
#
#         # Save AI answer
#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": answer
#             }
#         )
#
#
#         # Refresh screen
#         st.rerun()


import streamlit as st
import tempfile
import os

from src.document_loader import load_document
from src.chunking import split_documents
from src.embeddings import create_embeddings
from src.vector_store import create_vector_db
from src.retriever import get_retriever
from src.llm import create_llm
from src.chatbot import get_answer


# -----------------------------
# Page Settings
# -----------------------------

st.set_page_config(
    page_title="AI RAG Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# -----------------------------
# CSS - Professional Chat UI
# -----------------------------

st.markdown("""
<style>

/* ---------- Global ---------- */
.stApp {
    background: radial-gradient(circle at top, #161b26 0%, #0b0e14 60%);
}

#MainMenu, footer, header {visibility: hidden;}

.block-container {
    padding-top: 2rem;
    max-width: 780px;
}

/* ---------- Header ---------- */
.app-header {
    text-align: center;
    margin-bottom: 1.8rem;
}

.app-header .badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(56,189,248,0.15));
    border: 1px solid rgba(99,102,241,0.35);
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 12px;
    color: #a5b4fc;
    font-weight: 600;
    letter-spacing: 0.03em;
    margin-bottom: 14px;
}

.app-header .title {
    font-size: 34px;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #93c5fd 60%, #6366f1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}

.app-header .subtitle {
    color: #8b93a7;
    font-size: 14.5px;
    margin-top: 6px;
}

/* ---------- Upload Card ---------- */
.upload-card {
    background: linear-gradient(180deg, #171c27 0%, #12161f 100%);
    border: 1px solid #262c3a;
    border-radius: 18px;
    padding: 22px 24px;
    margin-bottom: 22px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

.upload-card .card-title {
    font-size: 16px;
    font-weight: 700;
    color: #e5e7eb;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
}

.upload-card .card-hint {
    color: #6b7280;
    font-size: 13px;
    margin-bottom: 14px;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 12.5px;
    font-weight: 600;
    margin-top: 10px;
}

.status-ready {
    background: rgba(34,197,94,0.12);
    color: #4ade80;
    border: 1px solid rgba(34,197,94,0.3);
}

.status-idle {
    background: rgba(148,163,184,0.1);
    color: #94a3b8;
    border: 1px solid rgba(148,163,184,0.25);
}

/* ---------- Chat Bubbles ---------- */
.chat-row {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 14px 0;
}

.chat-row.user {
    flex-direction: row-reverse;
}

.avatar {
    width: 34px;
    height: 34px;
    min-width: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

.avatar.user-avatar {
    background: linear-gradient(135deg, #6366f1, #2563eb);
}

.avatar.ai-avatar {
    background: linear-gradient(135deg, #0ea5e9, #14b8a6);
}

.bubble {
    padding: 12px 16px;
    border-radius: 16px;
    max-width: 78%;
    font-size: 14.5px;
    line-height: 1.55;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
}

.bubble.user-bubble {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    border-bottom-right-radius: 4px;
}

.bubble.ai-bubble {
    background: #1a1f2b;
    color: #e5e7eb;
    border: 1px solid #262c3a;
    border-bottom-left-radius: 4px;
}

.bubble .sender-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    opacity: 0.65;
    display: block;
    margin-bottom: 4px;
}

/* ---------- Buttons ---------- */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.55rem 1rem !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    box-shadow: 0 4px 14px rgba(37,99,235,0.35) !important;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(37,99,235,0.5) !important;
}

/* ---------- Chat Input ---------- */
[data-testid="stChatInput"] {
    border-radius: 14px !important;
}

/* ---------- Empty state ---------- */
.empty-state {
    text-align: center;
    color: #6b7280;
    padding: 30px 10px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
    <div class="app-header">
        <div class="badge">✨ Retrieval-Augmented Generation</div>
        <p class="title">🤖 AI RAG Chatbot</p>
        <p class="subtitle">Upload a document and chat with it — powered by your own data</p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "llm" not in st.session_state:
    st.session_state.llm = None

if "doc_name" not in st.session_state:
    st.session_state.doc_name = None


# -----------------------------
# Document Upload Card
# -----------------------------

st.markdown('<div class="upload-card">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card-title">📄 Upload Document</div>
    <div class="card-hint">Supported formats: PDF, DOCX, TXT, CSV, XLSX</div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["pdf", "docx", "txt", "csv", "xlsx"],
    label_visibility="collapsed"
)

if uploaded_file:

    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption(f"📎 **{uploaded_file.name}**  ·  {uploaded_file.size / 1024:.1f} KB")

    process_button = st.button(
        "⚙️ Process Document",
        use_container_width=True
    )

    if process_button:

        with st.spinner("Processing document..."):

            try:

                file_extension = os.path.splitext(uploaded_file.name)[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=file_extension
                ) as temp_file:

                    temp_file.write(uploaded_file.getbuffer())
                    file_path = temp_file.name

                documents = load_document(file_path)
                chunks = split_documents(documents)
                embeddings = create_embeddings()
                vector_store = create_vector_db(chunks, embeddings)
                retriever = get_retriever(vector_store)
                llm = create_llm()

                st.session_state.retriever = retriever
                st.session_state.llm = llm
                st.session_state.doc_name = uploaded_file.name

                os.remove(file_path)

                st.success("✅ Document processed successfully! You can start chatting now.")

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Status pill
if st.session_state.retriever is not None:
    st.markdown(
        f'<span class="status-pill status-ready">🟢 Ready · {st.session_state.doc_name}</span>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<span class="status-pill status-idle">⚪ No document processed yet</span>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Chat History
# -----------------------------

if not st.session_state.messages:
    st.markdown(
        '<div class="empty-state">💬 Your conversation will appear here.<br>Upload a document above and ask your first question!</div>',
        unsafe_allow_html=True
    )

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="chat-row user">
                <div class="avatar user-avatar">🧑</div>
                <div class="bubble user-bubble">
                    <span class="sender-label">You</span>
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="chat-row ai">
                <div class="avatar ai-avatar">🤖</div>
                <div class="bubble ai-bubble">
                    <span class="sender-label">AI Assistant</span>
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input("Ask something about your document...")

if question:

    if st.session_state.retriever is None:
        st.warning("⚠️ Please upload and process a document first.")

    else:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.spinner("Thinking..."):
            answer = get_answer(
                question,
                st.session_state.retriever,
                st.session_state.llm
            )

        st.session_state.messages.append({"role": "assistant", "content": answer})

        st.rerun()
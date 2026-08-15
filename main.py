from src.document_loader import load_document
from src.chunking import split_documents
from src.embeddings import create_embeddings
from src.vector_store import create_vector_db
from src.retriever import get_retriever
from src.llm import create_llm
from src.chatbot import get_answer


# Document load karo
documents = load_document("data/Ai_Research.pdf")
 # Document ko chunks mein divide karna h ab
chunks = split_documents(documents)

# Embedding model banana h ab
embeddings = create_embeddings()

# ChromaDB
vector_db = create_vector_db(chunks, embeddings)

# Retriever
retriever = get_retriever(vector_db)

# LLM
llm = create_llm()


# User ka question
question = input("Ask your question: ")

# Answer gennerate karaygay ab
answer = get_answer(
    question,
    retriever,
    llm
)

print("\nAnswer:")
print(answer)
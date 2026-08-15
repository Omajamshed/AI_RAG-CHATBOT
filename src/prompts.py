from langchain_core.prompts import ChatPromptTemplate
def get_rag_prompt():

    prompt = ChatPromptTemplate.from_template("""
You are an AI document assistant.

Answer the question using the information
from the uploaded documents.

If the answer is not available in the documents,
say that you could not find the information.
Give clear and accurate answers.
Context:
{context}
Question:
{question}
Answer:
""")
    return prompt

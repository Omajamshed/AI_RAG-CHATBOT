from langchain_google_genai import ChatGoogleGenerativeAI


def create_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key="OMA"

    )

    return llm
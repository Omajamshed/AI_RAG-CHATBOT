from langchain_core.chat_history import InMemoryChatMessageHistory

def create_memory():
    memory = InMemoryChatMessageHistory()
    return memory
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI


def load_llama_index(
    data_path: str = "src/ai_hub/navigation/hostel_helper/data",
) -> VectorStoreIndex:
    Settings.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    documents = SimpleDirectoryReader(data_path).load_data()
    return VectorStoreIndex.from_documents(documents)

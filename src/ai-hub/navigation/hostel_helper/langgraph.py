# Used to build the Streamlit web interface
import streamlit as st

# Provides access to environment variables and file system operations
import os

# Regular expression operations for pattern matching and text cleaning
import re

# Generates unique identifiers for each user session to support persistent memory
import uuid

# Typing helpers for structured and strongly typed dictionaries
from typing import TypedDict, List

# LLM interface for interacting with OpenAI's chat models like GPT-4
from langchain.chat_models import ChatOpenAI

# Loads plain text files as LangChain Document objects
from langchain.document_loaders import TextLoader

# Splits large text into smaller overlapping chunks for efficient retrieval
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Vector store implementation using FAISS for fast similarity-based search
from langchain.vectorstores import FAISS

# Converts text into dense vector representations using OpenAI's embedding API
from langchain.embeddings import OpenAIEmbeddings

# Creates and manages stateful execution graphs for multi-step workflows
from langgraph.graph import StateGraph, END

# In-memory checkpoint system for storing intermediate graph state
from langgraph.checkpoint.memory import MemorySaver

# Defines the schema for LangChain Document objects used in retrieval and processing
from langchain.schema import Document

# === STREAMLIT SESSION SETUP ===
# Initialize session state variables if they don't exist
CHAT_KEY = "messages_langgraph_chat"
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = []

# Generate and store a thread_id to track session execution in LangGraph
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# Set the title of the Streamlit app
st.title("🤖 Hostel Helper Chatbot - LangGraph")

# === LOAD AND PREPARE RAG COMPONENTS ===
# Attempt to load and process the hostel information document
try:
    # Load the Markdown document containing hostel information
    loader = TextLoader("src/ai-hub/navigation/hostel_helper/data/hostel_info.md")
    documents = loader.load()

    # Split the document into smaller chunks for efficient retrieval
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    # Retrieve the OpenAI API key from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Create a vector store from the document chunks using OpenAI embeddings
    vectorstore = FAISS.from_documents(
        chunks, OpenAIEmbeddings(openai_api_key=openai_api_key)
    )

    # Create a retriever from the vector store
    retriever = vectorstore.as_retriever()

    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(openai_api_key=openai_api_key)

except Exception:
    # Display an error message if any of the above steps fail
    st.error("Failed to load components.")
    st.stop()


# === DEFINE LANGGRAPH STATE SCHEMA ===
# Define the expected structure of the state that flows through the graph
class GraphState(TypedDict):
    question: str
    docs: List[Document]
    answer: str


# === DEFINE LANGGRAPH NODES ===


# Define the 'retrieve' node function
def retrieve_node(state: GraphState) -> GraphState:
    """
    Retrieves relevant documents based on the user's question.
    """
    question = state["question"]
    docs = retriever.get_relevant_documents(question)
    return {**state, "docs": docs}


# Define the 'generate' node function
def generate_node(state: GraphState) -> GraphState:
    """
    Generates an answer using the LLM based on the retrieved documents.
    """
    prompt = state["question"]
    docs = state["docs"]
    answer = llm.invoke(f"Answer based on context:\n\n{docs}\n\nQ: {prompt}")
    return {**state, "answer": answer.content}


# === BUILD THE LANGGRAPH ===

# Initializes a new LangGraph instance using a predefined state schema.
# This schema (GraphState) defines the expected input/output structure for each
# node in the graph.
graph_builder = StateGraph(GraphState)

# Registers the 'retrieve' node in the graph.
# This node is responsible for retrieving relevant documents based on the user question.
graph_builder.add_node("retrieve", retrieve_node)

# Registers the 'generate' node in the graph.
# This node uses the LLM to generate an answer using the retrieved documents.
graph_builder.add_node("generate", generate_node)

# Sets the starting point of the graph.
# When the graph is executed, it will begin at the 'retrieve' node.
graph_builder.set_entry_point("retrieve")

# Defines the path of execution from the 'retrieve' node to the 'generate' node.
# After retrieving documents, the graph proceeds to generate a response.
graph_builder.add_edge("retrieve", "generate")

# Marks the 'generate' node as the final step in the execution path.
# Once the answer is generated, the graph ends its execution.
graph_builder.add_edge("generate", END)


# Initialize memory and compile the graph with checkpointer
memory = MemorySaver()
agent_executor = graph_builder.compile(checkpointer=memory)

# === DISPLAY CHAT HISTORY ===
# Iterate through the stored messages and display them
for message in st.session_state[CHAT_KEY]:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            # Extract image links from the assistant's message
            links = re.findall(r"https://cf\.bstatic\.com[^)\s]+", message["content"])

            # Remove image markdown links from the message content
            cleaned = re.sub(
                r"\[.*?\]\((https://cf\.bstatic\.com[^)\s]+)\)", "", message["content"]
            )

            # Display the cleaned message content
            st.markdown(cleaned.strip())

            # Display each extracted image
            for link in links:
                st.image(link)
        else:
            # Display the user's message
            st.markdown(message["content"])

# === HANDLE USER INPUT ===
# Wait for user input in the chat input field
if prompt := st.chat_input("Type your message here..."):
    # Append the user's message to the session state
    st.session_state[CHAT_KEY].append({"role": "user", "content": prompt})

    # Display the user's message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show a loading spinner while generating the assistant's response
    with st.spinner("Thinking..."):
        # Execute the LangGraph agent with the user's question
        output = agent_executor.invoke(
            {"question": prompt},
            config={"configurable": {"thread_id": st.session_state.thread_id}},
        )
        bot_reply = output["answer"]

    # Append the assistant's response to the session state
    st.session_state[CHAT_KEY].append({"role": "assistant", "content": bot_reply})

    # Display the assistant's response
    with st.chat_message("assistant"):
        # Extract image links from the assistant's response
        links = re.findall(r"https://cf\.bstatic\.com[^)\s]+", bot_reply)

        # Remove image markdown links from the response content
        cleaned = re.sub(r"\[.*?\]\((https://cf\.bstatic\.com[^)\s]+)\)", "", bot_reply)

        # Display the cleaned response content
        st.markdown(cleaned.strip())

        # Display each extracted image
        for link in links:
            st.image(link)

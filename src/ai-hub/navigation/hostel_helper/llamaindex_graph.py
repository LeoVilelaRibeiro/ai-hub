# Used to build the Streamlit web interface
import streamlit as st

# Regular expression operations for pattern matching and text cleaning
import re

# Generates unique identifiers for each user session to support persistent memory
import uuid

# Typing helpers for structured and strongly typed dictionaries
from typing import TypedDict

# Creates and manages stateful execution graphs for multi-step workflows
from langgraph.graph import StateGraph, END

# In-memory checkpoint system for storing intermediate graph state
from langgraph.checkpoint.memory import MemorySaver

# LlamaIndex loader function (replaces vectorstore + retriever setup)
from navigation.hostel_helper.utils.llamaindex import load_llama_index

# === STREAMLIT SESSION SETUP ===
# Initialize session state variables if they don't exist
CHAT_KEY = "messages_llamaindex_graph"
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = []

# Generate and store a thread_id to track session execution in LangGraph
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# Set the title of the Streamlit app
st.title("🤖 Hostel Helper Chatbot - LlamaIndex + Langgraph")

# === LOAD AND PREPARE RAG COMPONENTS ===
# Use LlamaIndex to load and index the hostel information document
try:
    index = load_llama_index()
    query_engine = index.as_query_engine()
except Exception:
    # Display an error message if any of the above steps fail
    st.error("Failed to load components.")
    st.stop()


# === DEFINE LANGGRAPH STATE SCHEMA ===
# Define the expected structure of the state that flows through the graph
class GraphState(TypedDict):
    question: str
    answer: str


# === DEFINE LANGGRAPH NODES ===


# Define the 'generate' node function
# This node performs both retrieval and generation using LlamaIndex
def generate_node(state: GraphState) -> GraphState:
    """
    Generates an answer using the LLM based on the user's question.
    """
    prompt = state["question"]
    response = query_engine.query(prompt)
    return {**state, "answer": response.response}


# === BUILD THE LANGGRAPH ===

# Initializes a new LangGraph instance using a predefined state schema.
# This schema (GraphState) defines the expected input/output structure for each
# node in the graph.
graph_builder = StateGraph(GraphState)

# Register the only node required — LlamaIndex handles retrieval internally
graph_builder.add_node("generate", generate_node)

# Define the execution flow and endpoint
graph_builder.set_entry_point("generate")
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

# Used to build the Streamlit web interface
import streamlit as st

# Regular expression operations for pattern matching and text cleaning
import re

# LlamaIndex loader function (replaces LangChain FAISS + chain loading)
from navigation.hostel_helper.utils.llamaindex import load_llama_index

# === STREAMLIT SETUP ===
CHAT_KEY = "messages_llamaindex_chat"
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = []

st.title("🤖 Hostel Helper Chatbot - LlamaIndex")

# === PREPARE RAG ===
# Loads a Markdown file containing hostel information and prepares it with LlamaIndex
# for use in a Retrieval-Augmented Generation (RAG) pipeline.

# Steps:
# 1. Load and index documents using LlamaIndex.
# 2. Use the query engine for semantic retrieval and LLM response.

try:
    index = load_llama_index()
    query_engine = index.as_query_engine()
except Exception:
    st.error(
        "An error occurred while initializing LlamaIndex. "
        "Please check your environment variables or model access."
    )
    st.stop()

# === MESSAGE LOOP ===
# message is a dictionary, not an object.
# It contains role and content keys.
# Used to build the visual chat interface and handle content like text and images.
for message in st.session_state[CHAT_KEY]:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            image_links = re.findall(
                r"https://cf\.bstatic\.com[^)\s]+", message["content"]
            )
            cleaned_reply = re.sub(
                r"\[.*?\]\((https://cf\.bstatic\.com[^)\s]+)\)", "", message["content"]
            )
            st.markdown(cleaned_reply.strip())
            for link in image_links:
                st.image(link)
        else:
            st.markdown(message["content"])

# Waits for user input in the chat input field and stores the message in session state
if prompt := st.chat_input("Type your message here..."):
    # Saves the user message to the chat history
    st.session_state[CHAT_KEY].append({"role": "user", "content": prompt})

    # Displays the user's message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Shows a loading spinner while generating the assistant's response
    with st.spinner("Thinking..."):
        # Executes the question-answering query using LlamaIndex
        response = query_engine.query(prompt)
        bot_reply = response.response

    # Saves the assistant's response to the chat history
    st.session_state[CHAT_KEY].append({"role": "assistant", "content": bot_reply})

    # Displays the assistant's response, with image rendering if any image links
    # are detected
    with st.chat_message("assistant"):
        # Extracts image URLs from the response
        image_links = re.findall(r"https://cf\.bstatic\.com[^)\s]+", bot_reply)

        # Removes image markdown links from the text to clean the response
        cleaned_reply = re.sub(
            r"\[.*?\]\((https://cf\.bstatic\.com[^)\s]+)\)", "", bot_reply
        )

        # Displays the cleaned text response
        st.markdown(cleaned_reply.strip())

        # Renders each image extracted from the assistant's response
        for link in image_links:
            st.image(link)

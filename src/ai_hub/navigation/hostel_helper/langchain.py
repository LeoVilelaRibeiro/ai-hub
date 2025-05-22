# Used to build the Streamlit web interface
import streamlit as st

# Regular expression operations for pattern matching and text cleaning
import re

# Provides access to environment variables and file system operations
import os

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

# Loads a question-answering chain that integrates retrieval and LLM response
from langchain.chains.question_answering import load_qa_chain

# Stores chat history to maintain context in multi-turn conversations
from langchain.memory import ConversationBufferMemory


# === STREAMLIT SETUP ===
CHAT_KEY = "messages_langchain_chat"
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

st.title("🤖 Hostel Helper Chatbot - Langchain")

# === PREPARE RAG ===
# Loads a Markdown file containing hostel information and splits it into smaller chunks
# for use in a Retrieval-Augmented Generation (RAG) pipeline.

# Steps:
# 1. Load the document using TextLoader.
# 2. Split the content into overlapping text chunks (chunk_size=500, chunk_overlap=50)
#    using RecursiveCharacterTextSplitter to preserve context between chunks.
# 3. The resulting chunks can be indexed in a vector store for semantic retrieval
#    during question answering.

# This preprocessing step enables efficient and context-aware retrieval from long
# documents.

try:
    loader = TextLoader("src/ai_hub/navigation/hostel_helper/data/hostel_info.md")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    openai_api_key = os.getenv("OPENAI_API_KEY")
    vectorstore = FAISS.from_documents(
        chunks, OpenAIEmbeddings(openai_api_key=openai_api_key)
    )
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(openai_api_key=openai_api_key)
    qa_chain = load_qa_chain(llm, chain_type="stuff")
except Exception:
    st.error(
        "An error occurred while initializing the model with the provided key. "
        "Please check you enviroment variables or contact OpenAI support if the "
        "issue persists."
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

    # Retrieves relevant documents from the vector store based on the user's prompt
    context_docs = retriever.get_relevant_documents(prompt)

    # Shows a loading spinner while generating the assistant's response
    with st.spinner("Thinking..."):
        # Executes the question-answering chain using the provided documents and user
        # query.
        # The QA chain takes a list of context documents (retrieved based on the
        # prompt)
        # and passes them along with the question to the LLM.
        # Internally, this usually formats a prompt like:
        #   "Given the following context, answer the question:
        #   \n[docs]\nQuestion: [prompt]"
        # The LLM then generates a response using both the documents and its own
        # reasoning.
        # Returns the assistant's answer as a string.
        response = qa_chain.run(input_documents=context_docs, question=prompt)
        bot_reply = response

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

import streamlit as st

st.title("🏨 About the Hostel Helper Assistant")

st.markdown(
    """
    The **Hostel Helper Assistant** is a modular chatbot interface built with
    **LlamaIndex**, **LangChain**, **LangGraph**, and **Streamlit**. It is designed to
    answer questions from guests using information extracted from a markdown file about
    the *MAN CAVE HOSTEL*.

    Whether a guest wants to know about check-in times, see room pictures, or learn
    about nearby attractions, the assistant responds naturally — backed by structured
    content.

    ---

    ## ⚙️ Technical Overview

    This assistant is implemented in four variations:

    ### 💬 `llamaindex_chat.py`: LlamaIndex Query Interface
    - Loads the `hostel_info.md` file and splits it into chunks.
    - Creates a vector index using LlamaIndex (internally backed by OpenAI embeddings).
    - Uses the LlamaIndex query engine to retrieve relevant chunks and generate
      answers.
    - Displays results in a simple linear chat interface.

    ### 🧠 `llamaindex_graph.py`: LangGraph + LlamaIndex Workflow
    - Uses the same LlamaIndex backend, but wraps the query logic in a LangGraph
    pipeline.
    - Defines a graph with:
        - `generate`: a single node that handles retrieval and response.
    - Includes persistent memory through `MemorySaver`.

    ### 🧾 `langchain.py`: Traditional LangChain RAG
    - Loads the markdown file and splits it into semantic chunks.
    - Embeds the content using OpenAI embeddings.
    - Stores vectors in a FAISS index.
    - Uses `load_qa_chain` from LangChain to answer queries from retrieved context.

    ### 🔁 `langgraph.py`: LangChain + LangGraph Workflow
    - Builds a two-node LangGraph pipeline using LangChain tools.
    - Nodes:
        - `retrieve`: gets documents using FAISS retriever.
        - `generate`: formats and sends prompt with context to ChatOpenAI.
    - Returns structured responses via LangGraph execution.

    These variations demonstrate different ways to orchestrate RAG-based assistants
    sing both declarative (LangGraph) and chain-based (LangChain, LlamaIndex) designs.

    ---

    ## 📁 Data Source

    The source of truth is a markdown file located at:

    ```
    src/ai-hub/navigation/hostel_helper/data/hostel_info.md
    ```

    This file includes:
    - 📷 Room images
    - 📜 House rules
    - 📝 Guest reviews
    - 📍 Local attractions

    ---

    ## 🔐 API Key Requirement

    To run the assistant, you must define the following environment variable:

    - `OPENAI_API_KEY`: authenticates access to the OpenAI models.

    Without this, the assistant cannot retrieve or generate responses.

    ---

    ## 🧪 Purpose

    This assistant demonstrates how **Retrieval-Augmented Generation** and
    **graph-based modular workflows** can turn static content into a
    conversational agent.

    Built with:
    - Python
    - Streamlit
    - LlamaIndex
    - LangChain
    - LangGraph

    Ideal for hotels, hostels, or any business looking to create a scalable,
    LLM-powered chatbot based on internal documentation.
    """
)

# 🚀 AI HUB – Data Science & MLOps Applications

The **AI HUB** is a centralized repository of modular applications focused on **Data Science**, **Machine Learning**, and **MLOps**. Each module demonstrates a specific capability using tools such as **Streamlit**, **LlamaIndex**, **LangChain**, **LangGraph**, **CrewAI**, and **Retrieval-Augmented Generation (RAG)**.

The goal of this repository is to provide clear, reproducible, and production-inspired examples of applied AI techniques.

---

## 🔍 Capabilities Demonstrated

- Conversational agents with contextual memory
- Retrieval-Augmented Generation using LlamaIndex and LangChain
- Workflow modeling with LangGraph
- Collaborative multi-agent systems with CrewAI
- Semantic document indexing and search
- Clean and modular UIs with Streamlit

---

## 📂 Project Modules

### 🤖 Hostel Helper
A suite of assistants powered by a markdown knowledge base describing the *Man Cave Hostel*. Multiple implementations are provided to showcase different techniques and tooling:

#### • llamaindex_chat.py
A minimal RAG chatbot interface using LlamaIndex:
- Loads a markdown document and splits into chunks
- Indexes content using OpenAI-powered embeddings
- Retrieves relevant context and generates natural responses
- Stateless chat interface using Streamlit

#### • llamaindex_graph.py
A graph-based chatbot using LangGraph + LlamaIndex:
- Uses LangGraph to model the conversation as a state graph
- Defines nodes for retrieval/generation using LlamaIndex query engine
- Adds memory and structure to the conversational flow

#### • langchain.py
A RAG assistant using the traditional LangChain approach:
- Loads and chunks a markdown document
- Embeds content using OpenAIEmbeddings and stores in FAISS
- Retrieves context and runs a QA chain with ChatOpenAI
- Uses Streamlit with memory-enabled chat session

#### • langgraph.py
A LangChain-powered assistant implemented as a state graph:
- Separates retrieval and generation into LangGraph nodes
- Tracks state and execution using a checkpointed memory
- Enables reproducible and extensible RAG workflows

---

### 📝 BlogBuilder
An automated article generator powered by a CrewAI pipeline:

- **Planner**: Designs outline, audience targeting, SEO strategy
- **Writer**: Creates a markdown-based blog post
- **Editor**: Refines grammar and format for publishing

Returns clean Markdown ready for web display.

---

### 🎬 MovieMate
A smart assistant that answers questions about movies using both internal and external tools:

- Uses local document search tools for movie metadata
- Integrates the TMDB API for rich external information
- Multi-agent CrewAI architecture with specialized agents

Supports dynamic question answering such as "What movies are similar to Matrix?"

---

## ⚙️ Development Setup

### Requirements
- Python **3.12+**
- [Poetry](https://python-poetry.org/docs/#installation)
- Make (optional, for development automation)

### Installation

```bash
git clone <repository_url>
cd ai-hub
poetry install
```

### Running in Development Mode

```bash
make run-dev
```

Or directly:

```bash
poetry run streamlit run src/ai-hub/streamlit_app.py \
  --server.port=8501 --server.runOnSave=true
```

---

## 🔐 Environment Configuration

The following environment variables must be set before running any application:

- `OPENAI_API_KEY` – Required for LLM queries and indexing
- `TMDB_API_KEY` – Required for TMDB integration in MovieMate

These can be configured via a `.env` file or exported directly in the shell.

---

## 🧰 Technology Stack

| Tool        | Purpose                                      |
|-------------|-----------------------------------------------|
| Streamlit   | Interactive front-end for AI applications     |
| LlamaIndex  | Document indexing and RAG-based retrieval     |
| LangGraph   | Declarative multi-step graph-based execution  |
| CrewAI      | Multi-agent coordination and task workflows   |
| OpenAI      | LLM completions and text embeddings            |
| Poetry      | Dependency and virtual environment management |
| Makefile    | Command automation                            |

---

This repository is intended for practitioners seeking structured examples of AI applications using modern frameworks, reusable agents, and scalable conversational retrieval systems.

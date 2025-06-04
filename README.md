# 🚀 AI HUB – Data Science & MLOps Applications

The **AI HUB** is a centralized collection of hands-on applications focused on **Data Science**, **Machine Learning**, and **MLOps**.

Rather than acting as a monolithic project, AI HUB presents a suite of **independent, modular pages**—each demonstrating a specific technique or architecture. These applications are meant to be **practical, production-inspired**, and easily extensible.

---

## 🌟 Project Purpose

* Explore real-world applications of DS, ML, and LLMs.
* Compare different strategies for solving similar problems (e.g., recommendation systems).
* Apply modular design principles to ensure each feature is reusable and self-contained.
* Combine classical ML with modern LLM-based workflows.
* Showcase MLOps practices including model serving, configuration via environment variables, and interface modularization.

---

## 🧠 Concepts Covered

* Data preprocessing, feature engineering, and filtering logic
* Classical ML methods like TF-IDF, cosine similarity, association rules, etc.
* Hosted inference using Hugging Face models via public APIs
* UI modularization with Streamlit components
* Use of LLMs for semantic tasks and entity extraction
* Configuration through environment variables

---

## 🔐 Required Environment Variables

Before launching the app, define the following:

| Variable           | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| `OPENAI_API_KEY`   | Required for modules using OpenAI embeddings or chat completion |
| `TMDB_API_KEY`     | Used for retrieving metadata from TMDB (Movie Database API)     |
| `HUGGING_FACE_KEY` | Enables usage of hosted models via Hugging Face Inference API   |

These can be placed in a `.env` file or exported via shell:

```bash
export OPENAI_API_KEY=...
export TMDB_API_KEY=...
export HUGGING_FACE_KEY=...
```

---

## ⚙️ Getting Started

### Requirements

* Python **3.12+**
* [Poetry](https://python-poetry.org/docs/#installation)
* Make (optional, for streamlined local development)

### Install and Run

```bash
git clone <repository_url>
cd ai-hub
poetry install
make run-dev
```

Or manually:

```bash
poetry run streamlit run src/ai-hub/streamlit_app.py \
  --server.port=8501 --server.runOnSave=true
```

---

## 🧰 Tech Stack

| Tool           | Purpose                               |
| -------------- | ------------------------------------- |
| Streamlit      | Frontend interface                    |
| pandas / NumPy | Data manipulation                     |
| scikit-learn   | Similarity models and vectorization   |
| MLxtend        | Association rules                     |
| Hugging Face   | Hosted models for inference           |
| Poetry         | Dependency and environment management |
| Make           | Developer automation                  |

---

**AI HUB** is designed as a launchpad for data-driven prototypes, serving as a sandbox for both classical ML and modern LLM-based solutions in a unified, visual interface.

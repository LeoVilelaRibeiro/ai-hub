import streamlit as st

st.title("🤖 About the CrewAI Assistants")

st.markdown(
    """
  This module showcases how autonomous **LLM-powered agents**, orchestrated via
  **CrewAI**, can be combined to create goal-driven assistants using **Streamlit**.

  Two interactive applications are featured in this group:

  ---

  ## 📝 BlogBuilder
  An intelligent blog generation assistant that builds high-quality articles from a
  single topic input. It follows a structured writing pipeline:

  1. **Content Planner**: Analyzes trends, keywords, and audience to design a
  strategic outline.
  2. **Content Writer**: Writes an insightful article based on the planner's structure.
  3. **Editor**: Polishes the article to align with journalistic standards and removes
  formatting not suitable for web rendering (e.g., code block markers).

  ✨ Output: A well-structured blog post in plain Markdown, ready for web publication.

  ---

  ## 🎬 MovieMate
  A conversational assistant that provides rich, real-time movie recommendations and
  information:

  1. **Movie Recommender**: Gathers insights and conducts semantic analysis using
  internal tools and knowledge bases.
  2. **Specialist Recommender**: Enhances responses using external data from the
  **TMDB API** and custom endpoints (e.g., `ConsultingExternalAPI`).

  🧩 Key features:
  - Personalized, polite, and informative answers
  - Multi-agent collaboration
  - Integration with search tools and external APIs

  Example prompt: *"What are some movies similar to Matrix?"*

  ---

  ## 🔐 Environment Configuration
  To function securely and correctly, both assistants rely on the following environment
  variables:

  - `OPENAI_API_KEY`: Enables access to LLMs used by agents
  - `TMDB_API_KEY`: Grants access to movie metadata (used by MovieMate)

  ❗️If any variable is missing, the assistant will fail gracefully with an error
  message.

  ---

  ## 🧠 Why CrewAI?
  CrewAI simplifies multi-agent collaboration by abstracting task delegation and
  execution into reusable workflows.

  It is ideal for use cases where:
  - Tasks need to be split between different expert roles
  - Output quality depends on multi-step validation and polishing

  Built with:
  - Python
  - Streamlit
  - CrewAI framework
  - External tools & APIs (TMDB, custom endpoints)

  This module is part of a modular hub of data science and AI applications.
  """
)

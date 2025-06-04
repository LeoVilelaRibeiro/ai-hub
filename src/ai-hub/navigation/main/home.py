import streamlit as st
import os

logo_path = os.path.join("src", "assets", "ai_logo.png")
st.image(logo_path, width=300)

st.title("AI HUB")

st.markdown(
    """
  Welcome to **AI HUB**, a curated showcase of practical applications in
  **Data Science**, **Machine Learning**, and **MLOps**.

  This platform brings together diverse real-world techniques—ranging from
  recommendation systems and information extraction to API-based inference—
  to illustrate how modular AI solutions can be built, tested, and deployed
  using best practices.

  Rather than focusing on a single use case, AI HUB demonstrates how
  different **models**, **datasets**, and **pipelines** can coexist and
  complement each other under a unified interface.

  ---

  ## ⚙️ Key Features
  - Realistic data pipelines with **public datasets**
  - Practical demonstrations of **MLOps** concepts
  - Integration with **LLMs** and external APIs (e.g. Hugging Face)
  - Modular and reusable components across apps

  ---

  ## 🔐 Environment Variables
  Some modules require external APIs. Make sure to define the following variables:

  - `OPENAI_API_KEY`: Used for OpenAI-powered features.
  - `TMDB_API_KEY`: Used for The Movie Database (TMDB) APIs.
  - `HUGGING_FACE_KEY`: Used to access Hugging Face Inference APIs.

  These should be set in your environment or a `.env` file for local development.

  ---

  ## 🔗 Repository
  """
)

col1, col2 = st.columns(2)
with col1:
    st.link_button("📁 GitHub Repository", "https://github.com/LeoVilelaRibeiro/ai-hub")

st.markdown("---")
st.caption("© 2025 AI HUB – All rights reserved.")

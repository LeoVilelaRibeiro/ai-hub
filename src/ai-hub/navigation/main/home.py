import streamlit as st
import os

logo_path = os.path.join("src", "assets", "ai_logo.png")
st.image(logo_path, width=300)

st.title("AI HUB")

st.markdown(
    """
    Developed by **[AI](https://www.linkedin.com/company/-ai/)**, this hub
    presents a curated portfolio of **Data Science** and **MLOps** applications.

    It demonstrates modular and production-inspired use of LLMs, orchestration
    frameworks,
    and semantic search pipelines. Each page explores a standalone AI capability, built
    to
    highlight the value of intelligent systems in realistic scenarios.

    ---

    ## 🧭 Explore the Modules

    - **Hostel Helper**: Conversational AI trained on internal hostel data using
    LangChain
      and LangGraph
    - **BlogBuilder**: Autonomous multi-agent system for generating SEO-optimized blog
    posts
    - **MovieMate**: LLM-powered movie Q&A assistant using internal guides and external
    APIs
    ---

    ## 🔗 Links
  """
)

col1, col2 = st.columns(2)
with col1:
    st.link_button("📁 GitHub Repository", "https://github.com/-AI/ai-hub")
with col2:
    st.link_button("🔗 LinkedIn Page", "https://www.linkedin.com/company/-ai/")

st.markdown("---")
st.caption("© 2024 AI – All rights reserved.")

import streamlit as st

st.title("🧠 About the CRF Named Entity Recognition")

st.markdown(
    """
  This module demonstrates a **Named Entity Recognition (NER)** model built using
  **Conditional Random Fields (CRF)**.

  It is designed to extract structured entities such as names, addresses, phone numbers,
  CPF, emails, and other relevant tokens from unstructured text.

  ---

  ## 🚀 How It Works
  The model leverages classical machine learning techniques, where text is tokenized,
  transformed into a set of handcrafted features (like prefixes, suffixes,
  capitalization, etc.), and then processed through a CRF model.

  This approach does not rely on deep learning or LLMs, making it lightweight and fast
  for demonstration purposes.

  ---

  ## 🔍 Considerations
  While this tool can effectively capture patterns in structured text, it is important
  to note that its accuracy may vary depending on the context, phrasing, and formatting
  of the input.

  As a classical model, it does not possess contextual understanding comparable to
  modern language models. Consequently, its predictions are based purely on surface
  patterns learned from the training data.

  This makes it ideal for showcasing how traditional NER models work, but it should
  not be considered production-grade for complex or highly variable texts.

  ---

  ## 🏗️ Key Features
  - Fast and lightweight.
  - Fully offline — no API keys or internet connection required.
  - Provides entity extraction based on token patterns.
  - Interactive interface for quick testing and exploration.

  ---

  ## 💡 Limitations
  - Sensitivity to spelling, formatting, and unseen token patterns.
  - May miss entities if input deviates significantly from patterns in the training
  data.
  - Not designed to generalize as effectively as transformer-based models.

  ---

  ## 🧠 Built With:
  - Python
  - Streamlit
  - PyCRFSuite

  This module is part of a broader collection of AI and data science demos within the
  AI Hub.
  """
)

import streamlit as st


st.title("🛡️ About the Toxicity Classifier")

st.markdown(
    """
  This module provides an interface to analyze the **toxicity** of a sentence
  using a model from **Hugging Face Inference API**.

  It allows users to input any text and receive classification scores indicating
  the level of toxicity, including labels such as insult, threat, and identity hate.

  ---

  ## 🤖 Model Used
  - **unitary/toxic-bert**
  - Trained to detect toxic language in English.
  - Handles multiple labels (multi-label classification), such as:
    - **Toxic**
    - **Severe Toxic**
    - **Obscene**
    - **Threat**
    - **Insult**
    - **Identity Hate**

  ---

  ## 🔍 How it works:
  - Sends your input to the **Hugging Face Inference API**.
  - The model analyzes the text and returns a score (0 to 1) for each label.
  - The response is shown in a JSON-like format, with scores and predictions.
  - Additionally, the app provides a **summary sentence** stating whether the input is
  considered toxic.

  ---

  ## 📦 Dependencies
  - Streamlit
  - requests (for HTTP calls to the API)

  ---

  ## 🌐 External API
  - The model runs on **Hugging Face’s hosted infrastructure**.
  - ⚠️ May require an API key with usage limits depending on the current Hugging Face
  policy.

  ---

  ## 🧠 Key Takeaways
  - Simple and intuitive interface for real-time toxicity evaluation.
  - No local model download or setup required.
  - Demonstrates how to integrate external ML models via API into a Streamlit app.

  ---

  ## 🏗️ Built with:
  - Python
  - Streamlit
  - Hugging Face Inference API
  """
)

import streamlit as st

st.title("🧠 About the Gender Classifier")

st.markdown(
    """
  This module demonstrates a simple yet effective **Gender Classifier** based on
  Brazilian first names.

  It leverages a **rule-based approach** using a pre-built dictionary that maps
  thousands of first names to their respective gender classifications:

  - `F` → Female
  - `M` → Male

  The classifier works by performing an exact name lookup (case-insensitive) in
  this dictionary. If the name is found, the associated gender is returned;
  otherwise, the result is `Not Found`.

  ---

  ## 🚀 How It Works
  1. The user provides a first name via the interface.
  2. The app searches for this name in the dictionary.
  3. The output displays the gender as either **Female**, **Male**, or **Not Found**.

  ---

  ## 🏗️ Key Features
  - Instantaneous lookup with O(1) performance.
  - No reliance on machine learning models or external APIs.
  - Fully offline and deterministic.
  - Clean and intuitive Streamlit interface.

  ---

  ## 🔧 Implementation Details
  - The database of names is structured as a native Python dictionary
  (`dict[str, str]`).
  - A simple utility function (`get_gender_by_name`) handles input sanitation and
  lookup logic.
  - The classifier is highly performant for demo purposes and educational use.

  ---

  ## 💡 Limitations
  - The classifier relies on exact matches.
  - It does not account for misspellings, nicknames, or unregistered names.
  - It only includes the dataset provided and does not infer gender for unseen names.

  ---

  ## 🏗️ Built With:
  - Python
  - Streamlit

  This demo is part of a broader collection of AI and data science demos.
  """
)

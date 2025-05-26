import streamlit as st


st.title("🎥 About the Movie Recommender")

st.markdown(
    """
  This module showcases different recommendation techniques applied to movies,
  using the **MovieLens dataset**.

  Each approach highlights a distinct strategy for generating recommendations,
  ranging from simple popularity-based suggestions to more advanced collaborative
  methods.

  ---

  ## 🔥 Popularity-Based
  - Recommends the most popular movies globally.
  - Based solely on the number of ratings a movie has received.
  - ❌ Does not consider your preferences or any input movie.

  ---

  ## 🔗 Association Rules
  - Recommends movies that are **frequently watched together** by the same users.
  - Based on **pairwise co-occurrence** (Market Basket Analysis style).
  - Example: *“Users who watched **The Matrix** also watched **Inception**.”*

  **How it works:**
  - Counts how often movies appear together in users' rating histories.
  - Displays pairs with the highest co-occurrence.

  ---

  ## 🤝 Collaborative Filtering
  - Recommends movies based on the behavior of **similar users**.
  - If users who liked **Movie A** also liked **Movie B**, then **Movie B** is
  recommended.
  - Uses **item-based collaborative filtering**, based on rating patterns.

  **How it works:**
  - Calculates correlations between movies using user ratings.
  - Filters out movies with too few common ratings to ensure meaningful similarity.

  ---

  ## 🎯 Content-Based Filtering
  - Recommends movies based on their **content features**, specifically genres.
  - Finds movies with genres similar to the selected movie.

  **How it works:**
  - Converts genres into text vectors using **TF-IDF**.
  - Computes **cosine similarity** between the selected movie and others.

  ---

  ## 📄 Dataset: MovieLens
  - Public dataset widely used for recommendation system research.
  - Contains:
    - Movies metadata (titles, genres).
    - User ratings (for collaborative and association methods).

  ---

  ## 🧠 Key Takeaways
  - This module demonstrates how different recommendation strategies work:
    - **Popularity-based:** What everyone likes.
    - **Association-based:** What is commonly watched together.
    - **Collaborative:** What people similar to you enjoy.
    - **Content-based:** What is similar in content.

  - Each method has strengths and limitations:
    - Popularity is simple but not personalized.
    - Association captures co-viewing patterns.
    - Collaborative adapts to user preferences.
    - Content-based works even without rating data.

  ---

  ## 🏗️ Built with:
  - Python
  - Streamlit
  - pandas
  - numpy
  - scikit-learn
  """
)

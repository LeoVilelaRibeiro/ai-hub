import streamlit as st
import pandas as pd
import os


st.title("🎬 Movie Popularity Recommender")

st.markdown(
    """
    This page displays the most popular movies based on the **MovieLens dataset**.

    Movies are ranked by **popularity**, calculated from the number of ratings they
    received.

    ---
  """
)


# ========= Load Dataset =========
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data/movielens")

    movies = pd.read_csv(os.path.join(data_dir, "movies.csv"))
    ratings = pd.read_csv(os.path.join(data_dir, "ratings.csv"))

    return movies, ratings


movies_df, ratings_df = load_data()

# ========= Calculate Popularity =========
st.subheader("🔥 Most Popular Movies")

# Count number of ratings per movie
popularity = (
    ratings_df.groupby("movieId")
    .size()
    .reset_index(name="num_ratings")
    .merge(movies_df, on="movieId")
    .sort_values(by="num_ratings", ascending=False)
)

# Select top N
top_n = st.slider("Select number of movies to display:", 5, 100, 20)

# Prepare dataframe for visualization
popularity_table = popularity.head(top_n).copy()
popularity_table = popularity_table.rename(
    columns={"title": "Title", "num_ratings": "Number of Ratings", "genres": "Genres"}
)
popularity_table["Genres"] = popularity_table["Genres"].str.replace("|", ", ")

# Select columns to display
popularity_table = popularity_table[["Title", "Number of Ratings", "Genres"]]

# Display as interactive dataframe
st.dataframe(
    popularity_table,
    use_container_width=True,
    hide_index=True,
)

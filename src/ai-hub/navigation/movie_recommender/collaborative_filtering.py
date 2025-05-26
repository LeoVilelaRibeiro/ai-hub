import streamlit as st
import pandas as pd
import numpy as np
import os

from navigation.movie_recommender.components.movie_selector import movie_selector


st.title("🤝 Collaborative Filtering")

st.markdown(
  """
  This page recommends movies based on **Collaborative Filtering**, using the **MovieLens dataset**.

  Given a movie you've watched, it suggests other movies that were rated by users who also rated the selected movie.

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

# ========= Parameters =========
st.subheader("⚙️ Parameters")

min_common_ratings = st.slider(
  "Minimum number of users who rated both movies",
  min_value=2,
  max_value=20,
  value=5,
  step=1,
)

min_movie_ratings = st.slider(
  "Minimum number of ratings a movie must have to be considered",
  min_value=10,
  max_value=200,
  value=30,
  step=10,
)

# ========= Filter movies with few ratings =========
movie_counts = ratings_df['movieId'].value_counts()
valid_movies = movie_counts[movie_counts >= min_movie_ratings].index

filtered_ratings = ratings_df[ratings_df['movieId'].isin(valid_movies)]
filtered_movies_df = movies_df[movies_df['movieId'].isin(valid_movies)]

# ========= Pivot ratings =========
pivot_table = filtered_ratings.pivot_table(
  index='userId',
  columns='movieId',
  values='rating'
)

# ========= Select Movie =========
st.subheader("🎬 Select a movie to get recommendations")
selected_movie = movie_selector(filtered_movies_df)

if not selected_movie:
  st.stop()

movie_id_to_title = dict(filtered_movies_df[['movieId', 'title']].values)
title_to_movie_id = {v: k for k, v in movie_id_to_title.items()}

selected_movie_id = title_to_movie_id.get(selected_movie)

if selected_movie_id not in pivot_table.columns:
  st.warning("⚠️ The selected movie is not present in the filtered dataset.")
  st.stop()

# ========= Compute Similarities =========
st.subheader("🔗 Recommended Movies")

# Ratings vector for the selected movie
target_ratings = pivot_table[selected_movie_id]

# Compute correlation with other movies
similarities = pivot_table.corrwith(target_ratings)

# Clean the result
similarities = similarities.dropna().sort_values(ascending=False)

# Filter by minimum number of common ratings
common_counts = pivot_table.notnull().astype(int).T.dot(
  pivot_table.notnull().astype(int)
)[selected_movie_id]

recommendations = pd.DataFrame({
  "Similarity": similarities,
  "Common Ratings": common_counts
}).reset_index()

recommendations = recommendations[
  (recommendations['movieId'] != selected_movie_id) &
  (recommendations['Common Ratings'] >= min_common_ratings)
]

if recommendations.empty:
  st.warning("⚠️ No recommendations found with the current parameters.")
else:
  recommendations = recommendations.merge(
    filtered_movies_df,
    on='movieId'
  ).sort_values(by='Similarity', ascending=False)

  recommendations = recommendations.rename(columns={"title": "Recommended Movie"})

  st.dataframe(
    recommendations[["Recommended Movie", "Similarity", "Common Ratings", "genres"]],
    use_container_width=True,
    hide_index=True,
  )

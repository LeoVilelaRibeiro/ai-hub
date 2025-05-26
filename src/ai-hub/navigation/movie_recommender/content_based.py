import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from navigation.movie_recommender.components.movie_selector import movie_selector


st.title("🎯 Content-Based Filtering")

st.markdown(
  """
  This page recommends movies based on **Content-Based Filtering**, using the **MovieLens dataset**.

  Given a movie you've watched, it suggests other movies with similar content, 
  based on their genres.

  ---
  """
)

# ========= Load Dataset =========
@st.cache_data
def load_data():
  current_dir = os.path.dirname(os.path.abspath(__file__))
  data_dir = os.path.join(current_dir, "data/movielens")

  movies = pd.read_csv(os.path.join(data_dir, "movies.csv"))

  return movies


movies_df = load_data()

# ========= Preprocess Genres =========
movies_df['genres'] = movies_df['genres'].replace('(no genres listed)', '')
movies_df['genres'] = movies_df['genres'].str.replace('|', ' ')

# ========= TF-IDF Vectorizer =========
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(movies_df['genres'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map movie titles to indices
indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()

# ========= Select Movie =========
st.subheader("🎬 Select a movie to get recommendations")
selected_movie = movie_selector(movies_df)

if not selected_movie:
  st.stop()

if selected_movie not in indices:
  st.warning("⚠️ The selected movie is not in the dataset.")
  st.stop()

idx = indices[selected_movie]

# Get pairwise similarity scores
sim_scores = list(enumerate(cosine_sim[idx]))

# Sort movies by similarity
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# Get top N recommendations (excluding itself)
top_n = st.slider("Number of recommendations", 5, 50, 10)

sim_scores = sim_scores[1: top_n + 1]

# Get movie indices
movie_indices = [i[0] for i in sim_scores]

# Prepare recommendations DataFrame
recommendations = movies_df.iloc[movie_indices].copy()
recommendations['Similarity'] = [i[1] for i in sim_scores]

# ========= Display =========
st.subheader("🔗 Recommended Movies")

st.dataframe(
  recommendations[["title", "genres", "Similarity"]].rename(
    columns={"title": "Recommended Movie"}
  ),
  use_container_width=True,
  hide_index=True,
)

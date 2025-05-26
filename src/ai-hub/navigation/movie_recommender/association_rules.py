import streamlit as st
import pandas as pd
import os
from collections import Counter
from itertools import combinations

from navigation.movie_recommender.components.movie_selector import movie_selector


st.title("🧠 Movie Association Rules (No Filters)")

st.markdown(
    """
        This page recommends movies based on **Association Rules**, using the
        **MovieLens dataset**.

        Given a movie you've watched, it suggests other movies frequently rated
        together by other users.

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

min_pair_count = st.slider(
    "Minimum number of co-occurrences to consider a recommendation",
    min_value=1,
    max_value=20,
    value=2,
    step=1,
)

# ========= Prepare Dataset (No Filter) =========
movie_id_to_title = dict(movies_df[["movieId", "title"]].values)

title_to_movie_id = {v: k for k, v in movie_id_to_title.items()}

user_movie_df = ratings_df.groupby("userId")["movieId"].apply(list).reset_index()

transactions = user_movie_df["movieId"].tolist()

# ========= Count Co-occurrence =========
pair_counts = Counter()

for transaction in transactions:
    movie_pairs = combinations(sorted(set(transaction)), 2)
    pair_counts.update(movie_pairs)

# ========= Select Movie =========
st.subheader("🎬 Select a movie to get recommendations")
selected_movie = movie_selector(movies_df)

if not selected_movie:
    st.stop()

selected_movie_id = title_to_movie_id.get(selected_movie)

# ========= Generate Recommendations =========
recommendations = []

for (a, b), count in pair_counts.items():
    if selected_movie_id in (a, b) and count >= min_pair_count:
        other_movie_id = b if a == selected_movie_id else a
        recommendations.append(
            {
                "Recommended Movie": movie_id_to_title.get(
                    other_movie_id, str(other_movie_id)
                ),
                "Co-occurrence Count": count,
            }
        )

if not recommendations:
    st.warning("⚠️ No recommendations found with the current parameters.")
else:
    recommendations_df = pd.DataFrame(recommendations).sort_values(
        by="Co-occurrence Count", ascending=False
    )
    st.subheader("🔗 Recommended Movies")
    st.dataframe(
        recommendations_df,
        use_container_width=True,
        hide_index=True,
    )

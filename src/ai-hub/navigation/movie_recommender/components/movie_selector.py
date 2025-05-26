import streamlit as st
import pandas as pd


def movie_selector(movies_df: pd.DataFrame, label: str = "🎬 Select a movie") -> str:
    """
    Display a movie selection dropdown with autocomplete based on the provided movies
    DataFrame.

    Args:
        movies_df (pd.DataFrame): A DataFrame containing at least a 'title' column
                                  with the list of movie titles to display.
        label (str, optional): The label shown above the dropdown.
                                Defaults to "🎬 Select a movie".

    Returns:
        str: The title of the selected movie.
    """
    movie_list = movies_df.sort_values("title")["title"].tolist()

    return st.selectbox(label, movie_list, placeholder="Type to search...", index=None)

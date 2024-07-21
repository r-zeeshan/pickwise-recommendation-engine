import streamlit as st
from model import RecommendationEngine

# Initialize the recommendation engine with caching
@st.cache_resource
def load_engine():
    return RecommendationEngine()

engine = load_engine()

# Streamlit application
st.title("Movie and TV Series Recommendation Engine")

# User input for movie/TV series name
title = st.text_input("Enter the name of the movie or TV series you watched:")

# Option to select whether it's a movie or TV series
option = st.selectbox("Is it a movie or a TV series?", ("Movie", "TV Series"))

# User input for number of recommendations
top_n = st.number_input("How many recommendations do you want?", min_value=1, max_value=20, value=10)

# Button to get recommendations
if st.button("Get Recommendations"):
    if title:
        try:
            if option == "Movie":
                recommendations = engine.get_movie_recommendations(title, top_n)
            else:
                recommendations = engine.get_tv_recommendations(title, top_n)
            
            st.write(f"Top {top_n} recommendations based on '{title}':")
            for i, recommendation in enumerate(recommendations, start=1):
                st.write(f"{i}. {recommendation}")
        except ValueError as e:
            st.error(e)
    else:
        st.error("Please enter the name of the movie or TV series.")

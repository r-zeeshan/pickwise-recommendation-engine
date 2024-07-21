import streamlit as st
from model import RecommendationEngine

@st.cache_resource
def load_engine():
    """
    Load and cache the RecommendationEngine to ensure it is instantiated only once during the session.

    Returns:
        RecommendationEngine: An instance of the RecommendationEngine class.
    """
    return RecommendationEngine()

engine = load_engine()

def main():
    """
    Main function to run the Streamlit application for the recommendation engine.
    """
    st.title("Movie and TV Series Recommendation Engine")

    # User input for movie/TV series name
    title = st.text_input("Enter the name of the movie or TV series you watched:")

    # Option to select whether it's a movie or TV series
    option = st.selectbox("Is it a movie or a TV series?", ("Movie", "TV Series"))

    # User input for number of recommendations
    top_n = st.number_input("How many recommendations do you want?", min_value=1, max_value=20, value=3)

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

    st.markdown(
        """
        <div class="footer">
            <p><strong>Disclaimer:</strong> The information provided on this website is for informational purposes only and is not intended as financial advice. Always do your own research before making any investment decisions.</p>
            <p>Developed By Zeeshan Hameed</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    
if __name__ == "__main__":
    main()

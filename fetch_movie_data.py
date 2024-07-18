# fetch_movie_data.py
import pandas as pd
from data_utils import fetch_all_pages, collect_detailed_data, API_KEY, BASE_URL

def fetch_movie_data():
    """
    Fetches movie data from an API, processes it, and saves it to a CSV file.

    This function fetches popular and top-rated movies from an API, combines them,
    collects detailed data for each movie, creates a pandas DataFrame, and saves
    the data to a CSV file named 'movies_data.csv'.

    Parameters:
    None

    Returns:
    None
    """
    popular_movies = fetch_all_pages(API_KEY, BASE_URL, 'movie/popular')
    top_rated_movies = fetch_all_pages(API_KEY, BASE_URL, 'movie/top_rated')

    all_movies = popular_movies + top_rated_movies

    all_movies = {movie['id']: movie for movie in all_movies}.values()

    detailed_movies = collect_detailed_data(API_KEY, BASE_URL, all_movies, 'movie')

    movies_df = pd.DataFrame(detailed_movies)
    movies_df.to_csv('data/movies_data.csv', index=False)
    print("Movie data has been saved to movies_data.csv")

if __name__ == "__main__":
    fetch_movie_data()

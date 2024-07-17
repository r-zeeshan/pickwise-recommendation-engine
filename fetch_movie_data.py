# fetch_movie_data.py
import pandas as pd
from data_utils import fetch_all_pages, collect_detailed_data, API_KEY, BASE_URL

def main():
    # Fetch all available pages for popular and top-rated movies
    popular_movies = fetch_all_pages(API_KEY, BASE_URL, 'movie/popular')
    top_rated_movies = fetch_all_pages(API_KEY, BASE_URL, 'movie/top_rated')

    # Combine the data
    all_movies = popular_movies + top_rated_movies

    # Remove duplicates based on ID
    all_movies = {movie['id']: movie for movie in all_movies}.values()

    # Collect detailed data
    detailed_movies = collect_detailed_data(API_KEY, BASE_URL, all_movies, 'movie')

    # Create DataFrame and save to CSV
    movies_df = pd.DataFrame(detailed_movies)
    movies_df.to_csv('movies_data.csv', index=False)
    print("Movie data has been saved to movies_data.csv")

if __name__ == "__main__":
    main()

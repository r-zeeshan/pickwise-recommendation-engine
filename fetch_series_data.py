# fetch_series_data.py
import pandas as pd
from data_utils import fetch_all_pages, collect_detailed_data, API_KEY, BASE_URL

def main():
    # Fetch all available pages for popular and top-rated TV shows
    popular_tv = fetch_all_pages(API_KEY, BASE_URL, 'tv/popular')
    top_rated_tv = fetch_all_pages(API_KEY, BASE_URL, 'tv/top_rated')

    # Combine the data
    all_tv = popular_tv + top_rated_tv

    # Remove duplicates based on ID
    all_tv = {tv['id']: tv for tv in all_tv}.values()

    # Collect detailed data
    detailed_tv = collect_detailed_data(API_KEY, BASE_URL, all_tv, 'tv')

    # Create DataFrame and save to CSV
    tv_df = pd.DataFrame(detailed_tv)
    tv_df.to_csv('tv_data.csv', index=False)
    print("TV data has been saved to tv_data.csv")

if __name__ == "__main__":
    main()

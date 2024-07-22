import pandas as pd
from data_utils import fetch_all_pages, collect_detailed_data, API_KEY, BASE_URL

def fetch_series_data():
    """
    Fetches series data from the API, processes it, and saves it to a CSV file.

    This function fetches popular and top-rated TV series data from the API,
    combines them into a single list, collects detailed data for each series,
    converts the data into a pandas DataFrame, and saves it to a CSV file.

    Parameters:
        None

    Returns:
        None
    """
    popular_tv = fetch_all_pages(API_KEY, BASE_URL, 'tv/popular')
    top_rated_tv = fetch_all_pages(API_KEY, BASE_URL, 'tv/top_rated')

    all_tv = popular_tv + top_rated_tv

    all_tv = {tv['id']: tv for tv in all_tv}.values()

    detailed_tv = collect_detailed_data(API_KEY, BASE_URL, all_tv, 'tv')

    tv_df = pd.DataFrame(detailed_tv)
    tv_df.to_csv('data/tv_data.csv', index=False)
    print("TV data has been saved to tv_data.csv")

if __name__ == "__main__":
    fetch_series_data()

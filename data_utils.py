import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('TMDB_API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_all_pages(api_key, base_url, endpoint):
    """
    Fetches all pages of data from an API endpoint.

    Args:
        api_key (str): The API key to authenticate the request.
        base_url (str): The base URL of the API.
        endpoint (str): The specific endpoint to fetch data from.

    Returns:
        list: A list of all the fetched data from all pages.

    Raises:
        None

    """
    all_data = []
    page = 1
    while True:
        url = f"{base_url}/{endpoint}"
        params = {'api_key': api_key, 'language': 'en-US', 'page': page}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json().get('results', [])
            all_data.extend(data)
            total_pages = response.json().get('total_pages', 1)
            if page >= total_pages:
                break
            page += 1
        else:
            print(f"Failed to fetch page {page} of {endpoint}: {response.status_code}")
            break
    return all_data

def fetch_details(api_key, base_url, endpoint, item_id):
    """
    Fetches details for a specific item using the provided API key, base URL, endpoint, and item ID.

    Args:
        api_key (str): The API key for authentication.
        base_url (str): The base URL of the API.
        endpoint (str): The endpoint for the specific item.
        item_id (str): The ID of the item to fetch details for.

    Returns:
        dict: A dictionary containing the details of the item.

    """
    url = f"{base_url}/{endpoint}/{item_id}"
    params = {'api_key': api_key, 'language': 'en-US'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch details for {endpoint[:-1]} {item_id}: {response.status_code}")
        return {}

def collect_detailed_data(api_key, base_url, items, endpoint):
    """
    Collects detailed data for a list of items.

    Parameters:
    - api_key (str): The API key for authentication.
    - base_url (str): The base URL of the API.
    - items (list): A list of items.
    - endpoint (str): The endpoint for fetching item details.

    Returns:
    - detailed_data (list): A list of detailed data for each item.
    """
    detailed_data = []
    for item in items:
        item_id = item['id']
        details = fetch_details(api_key, base_url, endpoint, item_id)
        detailed_data.append(details)
    return detailed_data

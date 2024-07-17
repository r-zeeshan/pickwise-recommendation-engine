# data_utils.py
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('TMDB_API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_all_pages(api_key, base_url, endpoint):
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
    url = f"{base_url}/{endpoint}/{item_id}"
    params = {'api_key': api_key, 'language': 'en-US'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch details for {endpoint[:-1]} {item_id}: {response.status_code}")
        return {}

def collect_detailed_data(api_key, base_url, items, endpoint):
    detailed_data = []
    for item in items:
        item_id = item['id']
        details = fetch_details(api_key, base_url, endpoint, item_id)
        detailed_data.append(details)
    return detailed_data

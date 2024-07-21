# Movie and TV Series Recommendation Engine

This project is a content-based recommendation engine for movies and TV series, built using Python and Streamlit. The engine leverages TF-IDF vectorization and cosine similarity to recommend similar movies or TV series based on the input title provided by the user.  

The application is deployed and can be accessed [here](https://pickwise.streamlit.app/).


## Features

- Fetch data from TMDB API for movies and TV series.
- Clean and preprocess the data for efficient use.
- Build a content-based recommendation engine using TF-IDF and cosine similarity.
- Interactive Streamlit web application for user input and displaying recommendations.

## Project Structure

- `data_utils.py`: Contains utility functions to fetch and process data from the TMDB API.
- `fetch_movie_data.py`: Script to fetch and save movie data from the TMDB API.
- `fetch_series_data.py`: Script to fetch and save TV series data from the TMDB API.
- `model.py`: Implementation of the `RecommendationEngine` class.
- `app.py`: Streamlit application to interact with the recommendation engine.
- `data/`: Directory to store cleaned and processed data files.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/recommendation-engine.git
    cd recommendation-engine
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your TMDB API key:

    Create a `.env` file in the root directory and add your TMDB API key:

    ```
    TMDB_API_KEY=your_tmdb_api_key
    ```

## Usage

### Fetch Data

1. To fetch movie data, run:

    ```bash
    python fetch_movie_data.py
    ```

    This will save the movie data to `data/movies_data.csv`.

2. To fetch TV series data, run:

    ```bash
    python fetch_series_data.py
    ```

    This will save the TV series data to `data/tv_data.csv`.

### Run the Streamlit Application

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open the URL provided by Streamlit in your web browser to interact with the application.

## Example Usage

Once the Streamlit application is running, you can:

1. Enter the name of a movie or TV series you watched.
2. Select whether it's a movie or TV series.
3. Specify the number of recommendations you want.
4. Click on "Get Recommendations" to see the top recommendations based on your input.

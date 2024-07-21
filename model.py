import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self, movies_file='data/cleaned_movies_data.csv', tv_file='data/cleaned_series_data.csv'):
        """
        Initialize the RecommendationEngine with data files for movies and TV series.

        Args:
            movies_file (str): Path to the cleaned movies data CSV file.
            tv_file (str): Path to the cleaned TV series data CSV file.
        """
        self.movies_data = pd.read_csv(movies_file)
        self.tv_data = pd.read_csv(tv_file)
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix_movies, self.tfidf_matrix_tv = self.vectorize_text_features()
        self.cosine_sim_movies, self.cosine_sim_tv = self.calculate_cosine_similarities()

    def vectorize_text_features(self):
        """
        Vectorize the text features using TF-IDF.

        Returns:
            tuple: TF-IDF matrices for movies and TV series.
        """
        # Fill missing values for the 'overview' column
        self.movies_data['overview'] = self.movies_data['overview'].fillna('')
        self.tv_data['overview'] = self.tv_data['overview'].fillna('')

        # Fit and transform the overview column for movies
        tfidf_matrix_movies = self.tfidf_vectorizer.fit_transform(self.movies_data['overview'])

        # Fit and transform the overview column for TV series
        tfidf_matrix_tv = self.tfidf_vectorizer.fit_transform(self.tv_data['overview'])

        return tfidf_matrix_movies, tfidf_matrix_tv

    def calculate_cosine_similarities(self):
        """
        Calculate the cosine similarity matrices for movies and TV series.

        Returns:
            tuple: Cosine similarity matrices for movies and TV series.
        """
        # Compute the cosine similarity matrix for movies
        cosine_sim_movies = cosine_similarity(self.tfidf_matrix_movies, self.tfidf_matrix_movies)

        # Compute the cosine similarity matrix for TV series
        cosine_sim_tv = cosine_similarity(self.tfidf_matrix_tv, self.tfidf_matrix_tv)

        return cosine_sim_movies, cosine_sim_tv

    def get_movie_recommendations(self, title, top_n=10):
        """
        Get top N movie recommendations based on the provided title.

        Args:
            title (str): The title of the movie to get recommendations for.
            top_n (int): The number of top recommendations to return. Default is 10.

        Returns:
            pandas.Series: Titles of the top N recommended movies.
        """
        if title not in self.movies_data['title'].values:
            raise ValueError(f"Movie '{title}' not found in the dataset.")

        # Get the index of the movie that matches the title
        idx = self.movies_data[self.movies_data['title'] == title].index[0]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.cosine_sim_movies[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top N most similar movies
        sim_scores = sim_scores[1:top_n+1]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top N most similar movies
        return self.movies_data['title'].iloc[movie_indices]

    def get_tv_recommendations(self, name, top_n=10):
        """
        Get top N TV series recommendations based on the provided name.

        Args:
            name (str): The name of the TV series to get recommendations for.
            top_n (int): The number of top recommendations to return. Default is 10.

        Returns:
            pandas.Series: Names of the top N recommended TV series.
        """
        if name not in self.tv_data['name'].values:
            raise ValueError(f"TV series '{name}' not found in the dataset.")

        # Get the index of the TV series that matches the name
        idx = self.tv_data[self.tv_data['name'] == name].index[0]

        # Get the pairwise similarity scores of all TV series with that TV series
        sim_scores = list(enumerate(self.cosine_sim_tv[idx]))

        # Sort the TV series based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top N most similar TV series
        sim_scores = sim_scores[1:top_n+1]

        # Get the TV series indices
        tv_indices = [i[0] for i in sim_scores]

        # Return the top N most similar TV series
        return self.tv_data['name'].iloc[tv_indices]

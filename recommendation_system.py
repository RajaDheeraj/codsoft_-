from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Sample dataset
data = {
    'Movie ID': [1, 2, 3, 4, 5],
    'Title': ['The Matrix', 'Titanic', 'John Wick', 'The Notebook', 'Interstellar'],
    'Genre': ['Sci-Fi, Action', 'Romance, Drama', 'Action, Thriller', 'Romance, Drama', 'Sci-Fi, Adventure']
}

# Create a DataFrame
movies = pd.DataFrame(data)

def recommend_movies(input_movie_title):
    # Combine genres into a single string (for vectorization)
    movies['Combined'] = movies['Genre']

    # Vectorize genres using CountVectorizer
    count_vectorizer = CountVectorizer()
    genre_matrix = count_vectorizer.fit_transform(movies['Combined'])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

    # Find the index of the input movie
    try:
        movie_idx = movies[movies['Title'].str.lower() == input_movie_title.lower()].index[0]
    except IndexError:
        return "Movie not found in the dataset. Try another title."

    # Get similarity scores for all movies
    similarity_scores = list(enumerate(cosine_sim[movie_idx]))

    # Sort movies based on similarity scores
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the top 3 recommended movies (excluding the input movie itself)
    recommendations = [movies.iloc[i[0]]['Title'] for i in sorted_movies[1:4]]

    return recommendations

# Example usage
if __name__ == "__main__":
    print("Available movies:", movies['Title'].tolist())
    user_movie = input("Enter a movie title you like: ")
    recommendations = recommend_movies(user_movie)
    print("\nRecommended movies for you:", recommendations)

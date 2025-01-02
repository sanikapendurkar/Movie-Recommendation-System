# Movie Recommendation System with Flask and Surprise

This is a simple movie recommendation system built using **Flask** and **Surprise** (a Python library for collaborative filtering). The system predicts user ratings for movies based on their preferences using **Singular Value Decomposition (SVD)**. It allows users to input their `user_id` and `movie_id` to receive a predicted rating for the movie.

## Features:
- Predicts movie ratings based on user and movie IDs.
- Built using Flask for the web interface.
- Uses **Surprise** for the recommendation algorithm (SVD).
- **Pandas** for dataset manipulation and loading movie/ratings data.

## Technologies Used:
- **Flask** (Python Web Framework)
- **Surprise** (Recommendation Library)
- **Pandas** (Data Manipulation)
- **HTML** (Frontend)

## Requirements:
- Python 3.x
- Flask
- pandas
- scikit-surprise

## Installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-flask.git
    cd movie-recommendation-flask
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download or ensure you have the following CSV datasets:
   - `movies.csv`: Contains movie details like `movieId` and `title`.
   - `ratings.csv`: Contains user ratings with columns `userId`, `movieId`, and `rating`.

   You can use publicly available datasets like the [MovieLens dataset](https://grouplens.org/datasets/movielens/).

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to interact with the movie recommendation system.

## How it Works:
- The system is built on **Collaborative Filtering** using **SVD** (Singular Value Decomposition) from the Surprise library.
- The user inputs their `user_id` and `movie_id` on the web interface.
- The app predicts the rating the user would give to that particular movie based on their previous ratings and the ratings of other similar users.

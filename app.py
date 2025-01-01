from flask import Flask, request, render_template
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

app = Flask(__name__)

# Load datasets
movies = pd.read_csv('datasets/movies.csv')
ratings = pd.read_csv('datasets/ratings.csv')

# Set up the reader and load the data into Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2)

# Use SVD (Singular Value Decomposition) for building the recommendation model
algo = SVD()
algo.fit(trainset)

@app.route('/')
def home():
    return render_template('index.html', rating=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    movie_id = int(request.form['movie_id'])
    
    # Predict the rating
    pred = algo.predict(user_id, movie_id)
    
    return render_template('index.html', rating=pred.est)

if __name__ == '__main__':
    app.run(debug=True)

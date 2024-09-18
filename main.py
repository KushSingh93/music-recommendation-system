from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset (make sure your CSV is located inside the 'data' folder)
data = pd.read_csv('data/music_data.csv')

# Create a user-song matrix for collaborative filtering
user_song_matrix = data.pivot(index='user_id', columns='song_id', values='danceability').fillna(0)

# Calculate user similarity using cosine similarity
user_similarity = cosine_similarity(user_song_matrix)

# Recommendation function based on collaborative filtering
def recommend_songs(user_id, top_n=3):
    user_index = user_id - 1  # Assuming user_id starts from 1 in your data
    similar_users = user_similarity[user_index]

    # Get the weighted sum of songs liked by similar users
    similar_songs = user_song_matrix.T.dot(similar_users) / similar_users.sum()

    # Get the top N songs
    top_songs = similar_songs.nlargest(top_n).index

    # Extract song details for the top N recommended songs
    recommended_songs = data[data['song_id'].isin(top_songs)][['song_id', 'artist', 'year']]

    # Convert the DataFrame to a list of dictionaries for easier use in the template
    recommended_songs_dict = recommended_songs.to_dict(orient='records')

    return recommended_songs_dict

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the user ID from the form
    user_id = int(request.form['user_id'])

    # Call the recommendation function
    recommendations = recommend_songs(user_id)

    # Pass the recommendations to the template for rendering
    return render_template('recommend.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
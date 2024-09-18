# Music Recommendation System

This project is a simple music recommendation system built using Python and Flask. It provides song recommendations based on collaborative filtering, leveraging users' past listening patterns and song features like danceability, energy, and valence.

## Features
- **Collaborative Filtering**: Recommends songs to users based on the preferences of similar users.
- **Audio Features**: Takes into account features like danceability, energy, and valence to suggest similar songs.
- **User Engagement**: Personalized recommendations to boost user engagement.

## Project Structure
- `main.py`: The Flask application that runs the server and recommendation logic.
- `data/music_data.csv`: The dataset used for the recommendations.
- `templates/index.html`: The homepage of the application where users input their User ID.
- `templates/recommend.html`: The page where song recommendations are displayed.

## How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/KushSingh93/music-recommendation-system.git

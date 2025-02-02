import pandas as pd
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import euclidean_distances

# Load dataset
df = pd.read_csv('spotify.csv')

# Data Cleaning
df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
df.dropna(inplace=True)
df['explicit'] = df['explicit'].astype(bool)

# Sample dataset with 1,000 songs
sample_size = 1000
sampled_data = df.sample(n=sample_size, random_state=42)

# Save the sampled dataset to a CSV file
sampled_data.to_csv("sampled_songs.csv", index=False)
print("\n✅ Sampled songs saved to 'sampled_songs.csv'. Please check this file to choose a song.")

# Convert relevant features to numeric
features = ["acousticness", "energy", "valence", "danceability"]
sampled_data[features] = sampled_data[features].apply(pd.to_numeric)

# Compute Euclidean distances
feature_matrix = sampled_data[features].values
distances = euclidean_distances(feature_matrix)

# Create a similarity graph
G = nx.Graph()
threshold = 0.1  # Adjust as needed

# Add nodes (songs) to the graph
for _, row in sampled_data.iterrows():
    G.add_node(row["track_id"], title=row["track_name"], artist=row["artists"], album=row["album_name"])

# Add edges based on similarity threshold
for i in range(len(sampled_data)):
    for j in range(i + 1, len(sampled_data)):
        if np.linalg.norm(feature_matrix[i] - feature_matrix[j]) < threshold:
            G.add_edge(sampled_data.iloc[i]["track_id"], sampled_data.iloc[j]["track_id"])

# Function to get similar song recommendations
def get_recommendations(song_title, artist_name, exclude_artist=True, top_n=5):
    """Finds similar songs based on input song title and artist name."""
    
    song_node = sampled_data[
        (sampled_data["track_name"].str.lower() == song_title.lower()) & 
        (sampled_data["artists"].str.lower() == artist_name.lower())
    ]
    
    if song_node.empty:
        print("\n❌ Song not found! Please check 'sampled_songs.csv' and try again.")
        return None
    
    track_id = song_node.iloc[0]["track_id"]
    similar_songs = list(G.neighbors(track_id))
    
    rec_df = sampled_data[sampled_data["track_id"].isin(similar_songs)]
    
    if exclude_artist:
        rec_df = rec_df[rec_df["artists"].str.lower() != artist_name.lower()]
    
    return rec_df[["track_name", "artists", "album_name"]].head(top_n)

# Interactive User Input
def main():
    """Runs the interactive recommendation system."""
    
    print("\n🎵 Welcome to the Song Recommendation System! 🎵")
    print("\n📄 Please check 'sampled_songs.csv' to see available songs before searching.\n")
    
    while True:
        song_title = input("Enter the song title: ").strip()
        artist_name = input("Enter the artist's name: ").strip()
        
        recommendations = get_recommendations(song_title, artist_name)
        
        if recommendations is not None and not recommendations.empty:
            print("\n🎶 Similar Songs Found! 🎶\n")
            print(recommendations.to_string(index=False))
        else:
            print("\n⚠️ No similar songs found. Try a different song!\n")
        
        again = input("\nDo you want to find another recommendation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n🎧 Thank you for using the Song Recommendation System! 🎧")
            break

# Run the interactive program
if __name__ == "__main__":
    main()

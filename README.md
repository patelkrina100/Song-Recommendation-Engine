# 🎵 Song Recommendation System

This **Song Recommendation System** allows users to find similar songs based on musical attributes such as **acousticness, energy, valence, and danceability**. Using a **similarity graph** and **Euclidean distances**, it suggests songs that match the input song's characteristics.

## 🚀 Features
- Loads and cleans a Spotify dataset.
- Samples **1,000 songs**, ensuring that **The Strokes' "Is This It" album** is included.
- Computes **song similarity** based on key musical features.
- Uses **NetworkX** to build a **graph-based recommendation system**.
- **Interactive user input** for easy song lookup.

## 🎮 How It Works
1. **Run the script** (`python script_name.py`).
2. **Enter a song title and artist name** when prompted.
3. **Get recommendations** for similar songs.
4. **Repeat or exit** the recommendation loop.


## 📂 Dataset Information
- The system uses a **sampled dataset** (`final_sampled_dataset.csv`) containing 1,000 songs.  
- **Not all songs are available** in this dataset.  
- **Before searching**, you may want to **review the dataset** to ensure your song exists.

## 🛠 Dependencies
This project requires the following Python libraries:
- `pandas`
- `numpy`
- `networkx`
- `scikit-learn`
- `tabulate` *(for a well-formatted output table)*

To install missing dependencies, run:
```bash
pip install pandas numpy networkx scikit-learn tabulate

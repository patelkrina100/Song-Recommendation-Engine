# 🎵 Song Recommendation System

This **Song Recommendation System** allows users to find similar songs based on musical attributes such as **acousticness, energy, valence, and danceability**. Using **Euclidean distances** and a **graph-based approach**, the system suggests songs that share similar characteristics.

## 🚀 Features

- Loads and cleans a **Spotify dataset**.
- Samples **1,000 songs** randomly for analysis.
- Saves the sampled songs to a file (`sampled_songs.csv`) for user reference.
- Computes **song similarity** using key musical features.
- Builds a **graph-based recommendation system** using NetworkX.
- **Interactive user input** for easy song lookup.

## 📏 Understanding Euclidean Distance

The **Euclidean Distance** is used to measure the similarity between songs. It calculates the straight-line distance between two points in a multi-dimensional space. In this system, each song is represented as a point in a 4-dimensional space defined by the features:

- **Acousticness** 🎵
- **Energy** ⚡
- **Valence** 😀
- **Danceability** 💃

The formula for **Euclidean Distance** between two songs **A** and **B** is:

\[
d(A, B) = \sqrt{(A_1 - B_1)^2 + (A_2 - B_2)^2 + ... + (A_n - B_n)^2}
\]

where each **A_n** and **B_n** represents a feature value of a song.  
A **lower Euclidean distance** means the songs are more similar.

## 📄 Usage Instructions

1. **Run the script** (`python script_name.py`).
2. **Check the file** `sampled_songs.csv` to see available songs.
3. **Enter a song title and artist name** when prompted.
4. **Receive recommendations** for similar songs.
5. **Repeat or exit** the recommendation loop.

## 📂 Output

- A CSV file `sampled_songs.csv` is created containing **1,000 sampled songs**.
- The system prints **song recommendations** based on user input.

## 🛠️ Technologies Used

- **Python**
- **Pandas** (for data manipulation)
- **NumPy** (for numerical computations)
- **NetworkX** (for graph-based recommendations)
- **Scikit-learn** (for Euclidean distance calculation)

## 🔹 Notes

- The system **only recommends songs from the sampled dataset (`sampled_songs.csv`)**.
- If a song is **not found**, check the file and pick a song from the list.
- The **threshold for similarity** can be adjusted in the script.


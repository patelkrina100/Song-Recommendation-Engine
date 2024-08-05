# Song-Recommendation-Engine

## Overview
This project involves developing a song recommendation engine using Neo4J and a dataset of 114,000 Spotify songs. The engine leverages Euclidean distance to measure musical similarity and generates personalized song recommendations. The project includes data preprocessing, graph database modeling, and Cypher queries.

## Project Description
The objective of this project was to build a general-purpose song recommendation system. By modeling songs and their properties as nodes in a graph database and connecting similar songs through edges, we aimed to recommend new music based on user preferences.

## Data
The dataset used in this project is a Spotify dataset from Kaggle, containing information on about 114,000 songs and their musical properties. The dataset includes fifty-two songs by The Strokes, including all songs from their album "Is This It".

## Methodology
### Data Preprocessing
When preparing our dataset, we loaded the Spotify CSV file into a Jupyter Python file. We cleaned the data by removing an unnamed column (likely an index column), then checked for missing values and converted the explicit column to a Boolean data type for consistency and easier analysis later on. We then removed any records with missing values to ensure the integrity of the dataset. We identified and separated songs by The Strokes from the album “Is This It” and determined the number of additional songs we needed to have a sample size of 1000. Then we randomly sampled additional songs from the dataset (excluding those by The Strokes) to reach the target sample size. We combined all of these songs into one cleaned dataset and exported this to use for Neo4j.

This methodology showcases a thoughtful approach to constructing a sample that both meets the project's specific requirements and maintains a broad enough diversity for the recommendation system. It ensures that the system is tested with songs from a specific artist (The Strokes) while also being generalizable across the dataset. This process aligns well with the goals outlined in the assignment, laying a solid foundation for building the graph database and generating song recommendations.

## Graph Database Modeling
### Nodes:
Each song becomes a node with properties such as track_id, title, artist, album, and 4 musical properties (acousticness, energy, valence, danceability).

### Edges:
Connections (SIMILAR) between songs are based on the similarity of their musical properties. Our threshold for similarity is a difference of less than 0.1 for acousticness, energy, valence, and danceability.

## Recommendation Algorithm
The algorithm leverages Euclidean distance to quantify the similarity between songs based on their musical properties, including acousticness, energy, valence, and danceability. This approach calculates the root of square differences between each corresponding property of two songs, effectively measuring the "distance" between them in a multidimensional space where each dimension represents a specific musical attribute.

Songs with a smaller Euclidean distance between them are considered more similar, as their properties are closer in value. In our system, we connect songs in the graph database with a SIMILAR relationship if their Euclidean distance falls below a predefined threshold. This ensures that only songs with sufficiently close musical properties are recommended as similar, maintaining the relevance and quality of the recommendations.

For example, if we want to find songs similar to "Someday" by The Strokes, our algorithm searches the graph for songs that are connected to it through the SIMILAR relationship. It filters out any songs by The Strokes to diversify the recommendations. This process relies on the precomputed Euclidean distances between songs, which were used to establish the SIMILAR relationships in the graph database during the initial data processing and modeling phase.

By incorporating Euclidean distance into our recommendation algorithm, we achieve a scientifically grounded method of identifying song similarity, which significantly enhances the personalized experience of discovering new music through our system.

## Results
### Graph Model:
The graph database contains 1200 nodes and 103434 edges.

### Recommendations:
Generated five song recommendations based on similarity to "Someday" by The Strokes, excluding songs by The Strokes.


## Usage
### Preprocess Data:
Run the data preprocessing script to clean and sample the dataset.

### Create Graph Database:
Use the provided Cypher queries to create and populate the Neo4J graph database.

### Generate Recommendations:
Execute the Cypher queries to generate and retrieve song recommendations.

## Contributors
Juan Cuesta
Krina Patel
Riva Shukla
Dennis Ho

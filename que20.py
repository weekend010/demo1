#20

import pandas as pd
import numpy as np

# Load the Iris dataset

iris_data = pd.read_csv(r"C:\Users\pujac\OneDrive\Desktop\dsml\IRIS.csv")

# Use only the numerical columns for clustering
X = iris_data.iloc[:, :-1].values  # Exclude the species column

# Set parameters
K = 3  # Number of clusters
max_iterations = 10  # Number of iterations

# Randomly initialize cluster centroids as one of the data points
np.random.seed(42)  # For reproducibility
centroids = X[np.random.choice(X.shape[0], K, replace=False)]

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# K-means clustering
for iteration in range(max_iterations):
    # Step 1: Assign each point to the nearest cluster
    clusters = [[] for _ in range(K)]
    for point in X:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)

    # Step 2: Update centroids to the mean of the assigned points
    new_centroids = []
    for cluster_points in clusters:
        new_centroids.append(np.mean(cluster_points, axis=0) if cluster_points else np.zeros(X.shape[1]))
    new_centroids = np.array(new_centroids)

    # Check for convergence (optional)
    if np.all(centroids == new_centroids):
        break
    centroids = new_centroids

# Print final cluster means
print("Final cluster means after {} iterations:".format(max_iterations))
for idx, centroid in enumerate(centroids, start=1):
    print(f"Cluster {idx}: {centroid}")

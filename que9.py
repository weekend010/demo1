#9

import numpy as np

# Given points
points = {
    'P1': np.array([0.1, 0.6]),
    'P2': np.array([0.15, 0.71]),
    'P3': np.array([0.08, 0.9]),
    'P4': np.array([0.16, 0.85]),
    'P5': np.array([0.2, 0.3]),
    'P6': np.array([0.25, 0.5]),
    'P7': np.array([0.24, 0.1]),
    'P8': np.array([0.3, 0.2])
}

# Initial centroids
m1 = np.array([0.1, 0.6])  # Centroid for Cluster #1
m2 = np.array([0.3, 0.2])  # Centroid for Cluster #2

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# Function to assign points to the closest centroid
def assign_to_cluster(points, m1, m2):
    cluster_1 = []
    cluster_2 = []
    for key, point in points.items():
        distance_to_m1 = euclidean_distance(point, m1)
        distance_to_m2 = euclidean_distance(point, m2)

        if distance_to_m1 < distance_to_m2:
            cluster_1.append(key)
        else:
            cluster_2.append(key)

    return cluster_1, cluster_2

# Function to update centroids
def update_centroid(points, cluster):
    cluster_points = [points[key] for key in cluster]
    return np.mean(cluster_points, axis=0)

# First assignment of points to clusters
cluster_1, cluster_2 = assign_to_cluster(points, m1, m2)

# Update centroids
new_m1 = update_centroid(points, cluster_1)
new_m2 = update_centroid(points, cluster_2)

# Output
print(f"Initial clusters:")
print(f"Cluster 1: {cluster_1} | Centroid: {m1}")
print(f"Cluster 2: {cluster_2} | Centroid: {m2}")

print(f"\nUpdated clusters after one iteration:")
print(f"Cluster 1: {cluster_1} | New Centroid: {new_m1}")
print(f"Cluster 2: {cluster_2} | New Centroid: {new_m2}")

# Answering the specific questions

# 1. Which cluster does P6 belong to?
distance_to_m1 = euclidean_distance(points['P6'], m1)
distance_to_m2 = euclidean_distance(points['P6'], m2)
if distance_to_m1 < distance_to_m2:
    print(f"\nP6 belongs to Cluster 1")
else:
    print(f"\nP6 belongs to Cluster 2")

# 2. What is the population of a cluster around m2?
print(f"\nPopulation around m2 (Cluster 2): {len(cluster_2)}")

# 3. What is the updated value of m1 and m2?
print(f"\nUpdated m1: {new_m1}")
print(f"Updated m2: {new_m2}")

#10

import numpy as np

# Given points
points = {
    'P1': np.array([2, 10]),
    'P2': np.array([2, 5]),
    'P3': np.array([8, 4]),
    'P4': np.array([5, 8]),
    'P5': np.array([7, 5]),
    'P6': np.array([6, 4]),
    'P7': np.array([1, 2]),
    'P8': np.array([4, 9])
}

# Initial centroids
m1 = np.array([2, 10])  # Centroid for Cluster #1
m2 = np.array([5, 8])   # Centroid for Cluster #2
m3 = np.array([1, 2])   # Centroid for Cluster #3

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# Function to assign points to the closest centroid
def assign_to_cluster(points, m1, m2, m3):
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    for key, point in points.items():
        distance_to_m1 = euclidean_distance(point, m1)
        distance_to_m2 = euclidean_distance(point, m2)
        distance_to_m3 = euclidean_distance(point, m3)

        # Assign to the closest centroid
        if distance_to_m1 < distance_to_m2 and distance_to_m1 < distance_to_m3:
            cluster_1.append(key)
        elif distance_to_m2 < distance_to_m1 and distance_to_m2 < distance_to_m3:
            cluster_2.append(key)
        else:
            cluster_3.append(key)

    return cluster_1, cluster_2, cluster_3

# Function to update centroids
def update_centroid(points, cluster):
    cluster_points = [points[key] for key in cluster]
    return np.mean(cluster_points, axis=0)

# First assignment of points to clusters
cluster_1, cluster_2, cluster_3 = assign_to_cluster(points, m1, m2, m3)

# Update centroids
new_m1 = update_centroid(points, cluster_1)
new_m2 = update_centroid(points, cluster_2)
new_m3 = update_centroid(points, cluster_3)

# Output the clusters and centroids
print(f"Initial clusters:")
print(f"Cluster 1: {cluster_1} | Centroid: {m1}")
print(f"Cluster 2: {cluster_2} | Centroid: {m2}")
print(f"Cluster 3: {cluster_3} | Centroid: {m3}")

print(f"\nUpdated clusters after one iteration:")
print(f"Cluster 1: {cluster_1} | New Centroid: {new_m1}")
print(f"Cluster 2: {cluster_2} | New Centroid: {new_m2}")
print(f"Cluster 3: {cluster_3} | New Centroid: {new_m3}")

# Answering the specific questions

# 1. Which cluster does P6 belong to?
distance_to_m1 = euclidean_distance(points['P6'], m1)
distance_to_m2 = euclidean_distance(points['P6'], m2)
distance_to_m3 = euclidean_distance(points['P6'], m3)
if distance_to_m1 < distance_to_m2 and distance_to_m1 < distance_to_m3:
    print(f"\nP6 belongs to Cluster 1")
elif distance_to_m2 < distance_to_m1 and distance_to_m2 < distance_to_m3:
    print(f"\nP6 belongs to Cluster 2")
else:
    print(f"\nP6 belongs to Cluster 3")

# 2. What is the population of a cluster around m3?
print(f"\nPopulation around m3 (Cluster 3): {len(cluster_3)}")

# 3. What is the updated value of m1, m2, m3?
print(f"\nUpdated m1: {new_m1}")
print(f"Updated m2: {new_m2}")
print(f"Updated m3: {new_m3}")

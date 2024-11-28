#19

import pandas as pd

# Load the Iris dataset

iris_data = pd.read_csv(r"C:\Users\pujac\OneDrive\Desktop\dsml\IRIS.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(iris_data.head())

# List unique species
print("\nUnique species in the dataset:")
print(iris_data['species'].unique())

# Filter data for each species and compute descriptive statistics
for species in iris_data['species'].unique():
    print(f"\nStatistical details for {species}:")
    species_data = iris_data[iris_data['species'] == species]
    stats = species_data.describe(percentiles=[0.25, 0.5, 0.75])
    print(stats)

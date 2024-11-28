#11

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset from CSV file
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\IRIS.csv"  # Replace with your CSV file path
iris_data = pd.read_csv(dataset_path)

# Display the first few rows to understand the dataset structure
print(iris_data.head())

# Ensure columns are named correctly and map the target column if needed
# (Assuming your CSV has similar column names and a target column)

# 1. List features and their types
print("\nFeatures and their types:")
for col in iris_data.columns[:-1]:  # Assuming the last column is the target column
    print(f"Feature: {col}, Type: {iris_data[col].dtype}")

print("\nTarget (Species) is nominal.")

# 2. Create histograms for each feature
for col in iris_data.columns[:-1]:  # Exclude the target column
    plt.figure(figsize=(8, 5))
    sns.histplot(data=iris_data, x=col, kde=True, bins=20, color='blue')
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

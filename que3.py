# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the path to your dataset file)
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\House Data.csv"
house_df = pd.read_csv(dataset_path)

# Filter numeric columns
numeric_columns = house_df.select_dtypes(include=['number'])

# Compute and display standard deviation
print("\nStandard Deviation:")
print(numeric_columns.std())

# Compute and display variance
print("\nVariance:")
print(numeric_columns.var())

# Compute and display percentiles (25th, 50th, 75th)
print("\nPercentiles (25th, 50th, 75th):")
percentiles = numeric_columns.quantile([0.25, 0.5, 0.75])
print(percentiles)

# Create histograms for each numeric feature
print("\nCreating histograms...")
for column in numeric_columns.columns:
    plt.figure(figsize=(6, 4))
    plt.hist(numeric_columns[column], bins=30, color='blue', alpha=0.7, edgecolor='black')
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

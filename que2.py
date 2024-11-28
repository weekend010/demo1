# Import necessary libraries
import pandas as pd

# Load the dataset (update the path to your dataset file)
# Assuming the dataset is in a CSV format
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\Telecom Churn.csv"
telecom_df = pd.read_csv(dataset_path)

# Display the first few rows of the dataset to understand its structure
print("Dataset Preview:")
print(telecom_df.head())

# Filter numerical columns to avoid operations on non-numeric data
numeric_columns = telecom_df.select_dtypes(include=['number'])

# Compute and display statistics for numerical columns
print("\nSummary Statistics:")

# Minimum value
print("\nMinimum Values:")
print(numeric_columns.min())

# Maximum value
print("\nMaximum Values:")
print(numeric_columns.max())

# Mean value
print("\nMean Values:")
print(numeric_columns.mean())

# Range (max - min)
print("\nRange (Maximum - Minimum):")
range_values = numeric_columns.max() - numeric_columns.min()
print(range_values)

# Standard deviation
print("\nStandard Deviation:")
print(numeric_columns.std())

# Variance
print("\nVariance:")
print(numeric_columns.var())

# Percentiles (e.g., 25th, 50th, 75th)
print("\nPercentiles (25th, 50th, 75th):")
percentiles = numeric_columns.quantile([0.25, 0.5, 0.75])
print(percentiles)

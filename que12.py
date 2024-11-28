#12

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset (assuming it's in a CSV file)
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\IRIS.csv"  # Replace with your dataset path
iris_data = pd.read_csv(dataset_path)

# Display the first few rows to confirm data loading
print(iris_data.head())

# 1. Create box plots for each feature in the dataset
features = iris_data.columns[:-1]  # Exclude the target column (assuming it's the last column)

for feature in features:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=iris_data, x=feature, color='lightblue')
    plt.title(f"Box Plot of {feature}")
    plt.xlabel(feature)
    plt.show()

# 2. Identify and discuss distributions and outliers
print("\nSummary statistics for each feature:")
summary_stats = iris_data[features].describe()
print(summary_stats)

# Identify outliers using the 1.5*IQR rule
for feature in features:
    Q1 = iris_data[feature].quantile(0.25)
    Q3 = iris_data[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = iris_data[(iris_data[feature] < lower_bound) | (iris_data[feature] > upper_bound)]

    print(f"\nFeature: {feature}")
    print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    print(f"Number of Outliers: {len(outliers)}")
    if not outliers.empty:
        print("Outlier Rows:")
        print(outliers)

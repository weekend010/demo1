
#4

features = ['Age', 'Income', 'Gender', 'Ms']

import math
import pandas as pd

# Load the dataset from the CSV file
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\Lipstick.csv"  # Update with your actual file path
data = pd.read_csv(dataset_path)

# Helper function to calculate entropy
def calculate_entropy(data, target_attribute):
    target_values = data[target_attribute].tolist()  # Convert the column to a list
    total_instances = len(target_values)
    value_counts = {value: target_values.count(value) for value in set(target_values)}

    entropy = 0
    for count in value_counts.values():
        probability = count / total_instances
        entropy -= probability * math.log2(probability)
    return entropy

# Helper function to calculate information gain
def calculate_information_gain(data, feature, target_attribute):
    total_entropy = calculate_entropy(data, target_attribute)
    feature_values = data[feature].tolist()  # Convert the column to a list
    total_instances = len(feature_values)

    # Split data by unique feature values
    value_counts = {value: feature_values.count(value) for value in set(feature_values)}

    # Weighted entropy for each subset
    weighted_entropy = 0
    for value, count in value_counts.items():
        subset = data[data[feature] == value]
        subset_entropy = calculate_entropy(subset, target_attribute)
        weighted_entropy += (count / total_instances) * subset_entropy

    # Information gain
    information_gain = total_entropy - weighted_entropy
    return information_gain

# Specify the target attribute and features
target_attribute = 'Buys'  # Replace with your actual target column name
features = ['Age', 'Income', 'Gender', 'Ms']  # Replace with your actual feature column names

# Calculate entropy of the target attribute
print(f"Entropy of the target attribute '{target_attribute}': {calculate_entropy(data, target_attribute)}\n")

# Calculate information gain for each feature
information_gains = {}
for feature in features:
    info_gain = calculate_information_gain(data, feature, target_attribute)
    information_gains[feature] = info_gain
    print(f"Information Gain for feature '{feature}': {info_gain}")

# Determine the root node
root_node = max(information_gains, key=information_gains.get)
print(f"\nThe root node is: {root_node}")

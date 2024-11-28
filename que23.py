#23

import pandas as pd
import numpy as np

# Create the dataset
data = {
    'Age': ['Young', 'Young', 'Middle', 'Old', 'Old', 'Old', 'Middle', 'Young', 'Young', 'Old', 'Young', 'Middle', 'Middle', 'Old'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'Medium'],
    'Married': ['No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No'],
    'Health': ['Fair', 'Good', 'Fair', 'Fair', 'Fair', 'Good', 'Good', 'Fair', 'Fair', 'Fair', 'Good', 'Good', 'Fair', 'Good'],
    'Class': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Frequency table for 'Age' with respect to 'Class'
freq_table = pd.crosstab(df['Age'], df['Class'])
print("Frequency Table for 'Age':")
print(freq_table)

# Calculate the entropy of the dataset (before any split)
def entropy(class_values):
    class_counts = class_values.value_counts(normalize=True)
    return -np.sum(class_counts * np.log2(class_counts))

# Total entropy before split (considering the whole dataset)
total_entropy = entropy(df['Class'])
print(f"\nTotal Entropy: {total_entropy}")

# Calculate the weighted entropy for each age group
weighted_entropy = 0
for age in df['Age'].unique():
    subset = df[df['Age'] == age]
    subset_entropy = entropy(subset['Class'])
    weight = len(subset) / len(df)
    weighted_entropy += weight * subset_entropy

print(f"\nWeighted Entropy after splitting on 'Age': {weighted_entropy}")

# Calculate information gain
information_gain = total_entropy - weighted_entropy
print(f"\nInformation Gain from splitting on 'Age': {information_gain}")

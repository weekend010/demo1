#15

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset (inbuilt in seaborn)
titanic_data = sns.load_dataset('titanic')

# Preview the dataset
print("First few rows of the Titanic dataset:")
print(titanic_data.head())

# Check for missing values in the 'fare' column and handle them if any
print("\nMissing values in the 'fare' column:", titanic_data['fare'].isnull().sum())

# Plot a histogram to visualize the distribution of 'fare'
plt.figure(figsize=(10, 6))
sns.histplot(titanic_data['fare'], bins=30, kde=True, color='blue')
plt.title('Distribution of Titanic Fare Prices', fontsize=16)
plt.xlabel('Fare', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

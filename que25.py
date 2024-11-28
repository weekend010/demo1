#25

import pandas as pd
import numpy as np

# Sample data
data = {
    'Age': [25, 30, 22, np.nan, 29, np.nan, 35, 30, 22],
    'Income': ['High', 'Medium', 'Low', 'Medium', 'High', 'Low', 'Medium', 'Medium', np.nan],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 60000, 40000, 55000, np.nan, 65000, 70000, 70000, np.nan],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Data Cleaning

# 1. Handling missing values:
# For numerical columns, we'll fill missing values with the mean of that column.
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
# For categorical columns, we'll fill missing values with the mode (most frequent value).
df['Income'] = df['Income'].fillna(df['Income'].mode()[0])

# 2. Removing duplicates
df = df.drop_duplicates()

# 3. Handling invalid entries
# Let's say we consider any salary greater than 100,000 to be an invalid entry and should be removed.
df = df[df['Salary'] <= 100000]

# 4. Ensure consistency in format
# Convert "Income" to a consistent format by capitalizing the first letter of each entry.
df['Income'] = df['Income'].str.capitalize()

# Display cleaned DataFrame
print("Cleaned DataFrame:")
print(df)
print("\n")

# Data Transformation

# 1. Convert 'Age' to an integer type (after filling missing values)
df['Age'] = df['Age'].astype(int)

# 2. Normalize the 'Salary' column using Min-Max scaling (for better analysis or modeling)
df['Salary'] = (df['Salary'] - df['Salary'].min()) / (df['Salary'].max() - df['Salary'].min())

# 3. Encode categorical columns like 'Income' and 'Gender' using label encoding.
df['Income'] = df['Income'].map({'High': 3, 'Medium': 2, 'Low': 1})  # Simple label encoding for 'Income'
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})  # Simple label encoding for 'Gender'

# Display transformed DataFrame
print("Transformed DataFrame:")
print(df)

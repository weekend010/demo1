#24

import pandas as pd
import numpy as np

# Example DataFrame for demonstration
data = {
    'Age': [25, 30, 22, np.nan, 29, np.nan, 35],
    'Income': ['High', 'Medium', 'Low', 'Medium', 'High', 'Low', 'Medium'],
    'Married': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', np.nan],
    'Health': ['Good', 'Fair', 'Fair', 'Good', 'Fair', 'Good', 'Fair'],
    'Salary': [50000, 60000, 40000, 55000, np.nan, 65000, 70000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# 1. Counting unique values of data
print("Unique values in each column:")
print(df.nunique())  # Count of unique values per column
print("\n")

# 2. Format of each column (data types)
print("Data types of each column:")
print(df.dtypes)  # Data types of each column
print("\n")

# 3. Converting variable data types
# Example: Convert 'Salary' from float to integer
df['Salary'] = df['Salary'].fillna(0).astype(int)  # First filling NaN with 0 before conversion
print("Data types after converting 'Salary' to int:")
print(df.dtypes)
print("\n")

# Example: Convert 'Age' from float to integer (after filling missing values)
df['Age'] = df['Age'].fillna(df['Age'].mean()).astype(int)  # Filling NaN with mean
print("Data types after converting 'Age' to int:")
print(df.dtypes)
print("\n")

# 4. Identifying missing values
print("Missing values in each column:")
print(df.isnull().sum())  # Count of missing values in each column
print("\n")

# 5. Filling in the missing values
# Filling missing values using mean for numeric columns and mode for categorical columns
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill NaN in 'Age' with mean
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())  # Fill NaN in 'Salary' with mean
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])  # Fill NaN in 'Married' with mode
df['Income'] = df['Income'].fillna(df['Income'].mode()[0])  # Fill NaN in 'Income' with mode
df['Health'] = df['Health'].fillna(df['Health'].mode()[0])  # Fill NaN in 'Health' with mode

print("DataFrame after filling missing values:")
print(df)
print("\n")

# Import necessary libraries
import pandas as pd

# Reading data from CSV
csv_file =r"C:\Users\pujac\OneDrive\Desktop\dsml\Titanic.csv" 
titanic_csv = pd.read_csv(csv_file)

# Reading data from XLS
# xls_file = "titanic.xls" 
# titanic_xls = pd.read_excel(xls_file)

# Displaying the first few rows to ensure data is loaded
print("Data from CSV:")
print(titanic_csv.head())
# print("\nData from XLS:")
# print(titanic_xls.head())

# Indexing and selecting data (select rows where Age > 30 and Survived == 1)
indexed_data = titanic_csv.set_index("PassengerId")
selected_data = indexed_data[(indexed_data["Age"] > 30) & (indexed_data["Survived"] == 1)]
print("\nSelected Data:")
print(selected_data)

# Sorting data by Age
sorted_data = titanic_csv.sort_values(by="Age")
print("\nData Sorted by Age:")
print(sorted_data.head())

# Describing attributes of the data
description = titanic_csv.describe()
print("\nDescription of Data:")
print(description)

# Checking data types of each column
data_types = titanic_csv.dtypes
print("\nData Types of Each Column:")
print(data_types)


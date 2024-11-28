#14

import pandas as pd

# Load the dataset
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\Covid Vaccine Statewise.csv"  # Replace with your dataset path
data = pd.read_csv(dataset_path)

# A. Describe the dataset
print("Dataset Information:")
print(data.info())
print("\nDataset Summary Statistics:")
print(data.describe(include='all'))
print("\nFirst few rows of the dataset:")
print(data.head())

# B. Number of Males vaccinated
# Assuming the dataset contains a column named 'Male(Individuals Vaccinated)'
total_males_vaccinated = data['Male(Individuals Vaccinated)'].sum()
print(f"\nTotal number of males vaccinated: {total_males_vaccinated}")

# C. Number of Females vaccinated
# Assuming the dataset contains a column named 'Female(Individuals Vaccinated)'
total_females_vaccinated = data['Female(Individuals Vaccinated)'].sum()
print(f"\nTotal number of females vaccinated: {total_females_vaccinated}")

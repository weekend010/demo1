#13

import pandas as pd

# Load the dataset
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\Covid Vaccine Statewise.csv"  # Replace with your dataset path
data = pd.read_csv(dataset_path)

# a. Describe the dataset
print("Dataset Information:")
print(data.info())
print("\nDataset Summary Statistics:")
print(data.describe(include='all'))
print("\nFirst few rows of the dataset:")
print(data.head())

# b. Number of persons state-wise vaccinated for the first dose in India
# Assuming 'First Dose Administered' column exists in the dataset
statewise_first_dose = data.groupby('State')['First Dose Administered'].sum().reset_index()
print("\nNumber of persons state-wise vaccinated for the first dose:")
print(statewise_first_dose)

# c. Number of persons state-wise vaccinated for the second dose in India
# Assuming 'Second Dose Administered' column exists in the dataset
statewise_second_dose = data.groupby('State')['Second Dose Administered'].sum().reset_index()
print("\nNumber of persons state-wise vaccinated for the second dose:")
print(statewise_second_dose)

# Optional: Save the results to CSV files
# statewise_first_dose.to_csv("/content/statewise_first_dose.csv", index=False)
# statewise_second_dose.to_csv("/content/statewise_second_dose.csv", index=False)

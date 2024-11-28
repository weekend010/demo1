#16

import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset using pandas
titanic = pd.read_csv(r'C:\Users\pujac\OneDrive\Desktop\dsml\Titanic.csv')

# Check the first few rows of the dataset
print(titanic.head())

# Plot the histogram for the 'Fare' column
plt.figure(figsize=(10, 6))
plt.hist(titanic['Fare'].dropna(), bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Ticket Fare for Titanic Passengers', fontsize=16)
plt.xlabel('Fare', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

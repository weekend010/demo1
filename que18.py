#18

import pandas as pd

# Load the House Price dataset

house_data = pd.read_csv(r"C:\Users\pujac\OneDrive\Desktop\dsml\House Data.csv")

# Display the first few rows of the dataset
print(house_data.head())

# Check unique entries in the 'price' column to identify issues
print(house_data['price'].unique())

# Clean and convert the 'price' column to numeric
# Remove 'TL', commas, and other non-numeric characters
house_data['price'] = house_data['price'].str.replace('TL', '', regex=False)
house_data['price'] = house_data['price'].str.replace(',', '', regex=False)
house_data['price'] = house_data['price'].str.extract('(\d+)', expand=False)  # Extract only numeric values
house_data['price'] = pd.to_numeric(house_data['price'], errors='coerce')  # Convert to float, set invalid entries to NaN

# Drop rows with NaN prices (optional, depending on the requirement)
house_data = house_data.dropna(subset=['price'])

# Categorical variable: district, Quantitative variable: price
grouped_stats = house_data.groupby('district')['price'].agg(['mean', 'median', 'min', 'max', 'std'])

# Rename the columns for clarity
grouped_stats.rename(columns={
    'mean': 'Mean Price',
    'median': 'Median Price',
    'min': 'Minimum Price',
    'max': 'Maximum Price',
    'std': 'Standard Deviation'
}, inplace=True)

# Display the grouped summary statistics
print(grouped_stats)

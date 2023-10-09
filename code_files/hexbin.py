import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
df = pd.read_csv('processed_data.csv')

# Remove the rows with 'YEAR' in 'Year' column
df = df[df['Year'] != 'YEAR']

# Convert 'Year' to integer type
df['Year'] = df['Year'].astype(int)

# Convert 'Measure' to numeric
df['Measure'] = pd.to_numeric(df['Measure'], errors='coerce')

# Create the hexbin plot
plt.hexbin(df['Year'], df['Measure'], gridsize=30, cmap='Blues')
cb = plt.colorbar(label='Count in bin')

plt.xlabel('Year')
plt.ylabel('Measure')

plt.show()

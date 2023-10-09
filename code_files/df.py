import pandas as pd

# Read the suicide rates CSV file
suicide_df = pd.read_csv('suicide_rates.csv')

# Select the relevant columns
suicide_df = suicide_df[['FullGeoName', 'YEAR', 'STATE', 'RATE', 'DEATHS']]

# Read the data table CSV file
data_table_df = pd.read_csv('data-table.csv')

# Merge the two dataframes based on the 'STATE' column
merged_df = pd.merge(suicide_df, data_table_df, on='STATE')

# Save the transformed data to a new CSV file
merged_df.to_csv('transformed_data.csv', index=False)

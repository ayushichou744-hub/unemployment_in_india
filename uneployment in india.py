import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('unemployment_in_india.csv')

# Print and inspect column names
print("Columns in your data:", df.columns.tolist())

# Option 1: Strip all column names (recommended)
df.columns = df.columns.str.strip()

# Display first few rows
print("Data preview:")
print(df.head())

# Continue with normal code, but update to match the fixed column names
# If your column is 'Estimated Unemployment Rate (%)'
rate_col = 'Estimated Unemployment Rate (%)'
date_col = 'Date'
region_col = 'Region'

# Convert 'Date' column to datetime
if date_col in df.columns:
    df[date_col] = pd.to_datetime(df[date_col])

# Plot by region
if region_col in df.columns and rate_col in df.columns:
    regions = df[region_col].unique()
    plt.figure(figsize=(10,6))
    for region in regions:
        region_data = df[df[region_col] == region]
        plt.plot(region_data[date_col], region_data[rate_col], label=region)
    plt.xlabel('Date')
    plt.ylabel('Estimated Unemployment Rate (%)')
    plt.title('Estimated Unemployment Rate by Region in India')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot national level
elif date_col in df.columns and rate_col in df.columns:
    plt.figure(figsize=(10,6))
    plt.plot(df[date_col], df[rate_col])
    plt.xlabel('Date')
    plt.ylabel('Estimated Unemployment Rate (%)')
    plt.title('Estimated Unemployment Rate in India Over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Cannot plot: Expected columns in the data are missing.")

# Summary stats
if rate_col in df.columns:
    print("Basic statistics for Estimated Unemployment Rate (%):")
    print(df[rate_col].describe())
else:
    print("Column for unemployment rate not found in the data.")
import pandas as pd
import glob

# Path pattern to match your CSV files, e.g., all CSVs in a folder
csv_files = glob.glob('/home/jo/Desktop/join/*.csv')

# List to hold data from each file
dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames vertically (stack rows)
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_output.csv', index=False)

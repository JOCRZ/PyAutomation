import os
import csv
import sys

# Define the output file name
output_file = "filenames.csv"

# The directory to search is passed as a command-line argument,
# or defaults to the current directory if none is provided.
target_dir = sys.argv[1] if len(sys.argv) > 1 else "."

# Open the CSV file for writing
try:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(['FileName', 'DirectoryPath'])

        # Walk through the directory and its subdirectories
        for root, _, files in os.walk(target_dir):
            for file in files:
                # Write the filename and its full directory path
                csv_writer.writerow([file, root])

    print(f"Successfully extracted file names to: {output_file}")

except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
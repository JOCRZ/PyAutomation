import csv
import os
import sys

# --- Configuration ---
CSV_FILENAME = 'rename_map.csv' # The name of your CSV file
RENAME_COLUMN = 'Rename'        # The header for the new sequence number
FILENAME_COLUMN = 'FileName'    # The header for the original filename

def rename_files_from_csv():
    """Reads a CSV file to get renaming instructions and renames files."""
    
    # 1. Check if the CSV file exists
    if not os.path.exists(CSV_FILENAME):
        print(f"🛑 Error: CSV file '{CSV_FILENAME}' not found. Ensure it is in the same directory.")
        sys.exit(1)

    rename_count = 0
    
    try:
        # 2. Read the CSV and create the renaming map
        with open(CSV_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Dictionary to store {old_filename: new_filename} mapping
            renaming_map = {}
            
            for row in reader:
                try:
                    old_filename = row[FILENAME_COLUMN]
                    # Get the new sequence number, ensure it's at least 2 digits for good sorting
                    new_number = f"{int(row[RENAME_COLUMN]):02d}"
                    
                    # Determine the file extension
                    _, ext = os.path.splitext(old_filename)
                    
                    # Create the new filename: [01, 02, etc.] + [original file name part after the number] + [.mp3]
                    # We strip off the original number/title to ensure a clean new name.
                    # This example keeps the text after the hyphen, like " - Night Changes.mp3"
                    
                    # Find the first hyphen in the original filename's text
                    if ' - ' in old_filename:
                        name_part = old_filename.split(' - ', 1)[1]
                        # Remove the original extension from the name part
                        name_part = name_part.replace(ext, '')
                        
                        new_filename = f"{new_number} - {name_part}{ext}"
                    else:
                         # Fallback for files without a hyphen structure, uses the whole old name
                        new_filename = f"{new_number} - {old_filename}"

                    renaming_map[old_filename] = new_filename
                    
                except ValueError:
                    print(f"⚠️ Warning: Could not process row due to invalid number in '{RENAME_COLUMN}' column: {row}")
                except KeyError as e:
                    print(f"🛑 Error: Column '{e.args[0]}' not found in CSV. Check your column headers.")
                    sys.exit(1)

        # 3. Apply the renaming
        print(f"Loaded {len(renaming_map)} renaming instructions. Starting rename...")
        
        for old_name, new_name in renaming_map.items():
            # Check if the file actually exists before trying to rename
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                print(f"✅ Renamed: '{old_name}' -> '{new_name}'")
                rename_count += 1
            else:
                print(f"❌ Skipped: File '{old_name}' not found.")

        print(f"\n✨ Renaming complete! {rename_count} files were successfully renamed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    rename_files_from_csv()
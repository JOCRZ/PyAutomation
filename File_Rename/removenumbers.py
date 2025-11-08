import os
import re

def rename_mp3_files(directory='.'):
    """
    Renames mp3 files in the specified directory by removing leading numbers (e.g., "01. Song.mp3" -> "Song.mp3").

    Args:
        directory (str): The path to the directory containing the files. Defaults to the current directory.
    """
    print(f"Starting to process files in directory: {os.path.abspath(directory)}\n")
    
    # Regular expression to match leading digits, optional space, dot, and optional space
    # Example matches: "01. ", "03 - ", "1. ", "01"
    # The (.*) captures the rest of the filename (the song title)
    # The re.IGNORECASE flag is for matching the .mp3 extension
    pattern = re.compile(r"^(\d+\s*[-.]?\s*)(.*\.mp3)$", re.IGNORECASE)
    
    renamed_count = 0
    
    try:
        # Loop through all files in the directory
        for filename in os.listdir(directory):
            # Construct the full path
            old_filepath = os.path.join(directory, filename)

            # Skip directories
            if os.path.isdir(old_filepath):
                continue

            # Check if the filename matches the pattern
            match = pattern.match(filename)
            
            if match:
                # Group 2 contains the desired new filename (the part after the track number)
                new_filename = match.group(2).strip()
                new_filepath = os.path.join(directory, new_filename)

                # Ensure the new filename isn't empty (though unlikely with the pattern)
                if new_filename:
                    # Check if the new filename already exists to avoid overwriting a different file
                    if os.path.exists(new_filepath) and old_filepath != new_filepath:
                        print(f"⚠️ **Skipping rename**: '{filename}' -> '{new_filename}' because a file with the new name already exists.")
                        continue
                        
                    # Perform the rename operation
                    os.rename(old_filepath, new_filepath)
                    print(f"✅ **Renamed**: '{filename}' -> '{new_filename}'")
                    renamed_count += 1
                else:
                    print(f"❌ **Skipping**: '{filename}' - New filename resulted in an empty string.")
            
            # Optional: Add an else block if you want to see files that *don't* match the pattern
            # else:
            #     if filename.lower().endswith('.mp3'):
            #         print(f"🔍 **No change**: '{filename}' (Does not match the numbering pattern)")
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")

    print(f"\n✨ **Finished renaming.** Total files renamed: **{renamed_count}**")

# --- EXECUTION ---
# Make sure to place this Python script in the same folder as your MP3 files, 
# or change the `directory` argument to the correct path.
if __name__ == "__main__":
    rename_mp3_files()

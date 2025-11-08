import os
import shutil

# Define the source directory where the files are downloaded
download_dir = "/home/jo/Downloads"

# Define the target directories for each file type
directories = {
    "image": "/home/jo/Pictures",
    "audio": "/home/jo/Music",
    "video": "/home/jo/Videos",
    "document": "/home/jo/Documents"
}

# Define the file extensions for each file type
file_types = {
    "image": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    "audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    "video": ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm'],
    "document": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv']
}

# Create target directories if they don't exist
for dir_path in directories.values():
    os.makedirs(dir_path, exist_ok=True)

# Function to move files based on their extension
def move_files():
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)
        
        # Ensure we're working with files, not directories
        if os.path.isfile(file_path):
            # Determine the file's extension
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Check which category the file extension belongs to
            for file_type, extensions in file_types.items():
                if file_ext in extensions:
                    # Move the file to the corresponding directory
                    target_dir = directories[file_type]
                    shutil.move(file_path, target_dir)
                    print(f"Moved {filename} to {target_dir}")
                    break
            else:
                print(f"No matching category for {filename}, file was not moved.")

# Run the file moving function
move_files()

from pydub import AudioSegment
import os

# Supported input formats
AUDIO_EXTENSIONS = [".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac", ".wma"]

def convert_folder_to_128kbps(folder_path):
    # Create output folder
    output_folder = os.path.join(folder_path, "converted_128kbps")
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        input_path = os.path.join(folder_path, file_name)

        # Skip folders
        if os.path.isdir(input_path):
            continue

        # Process only audio files
        ext = os.path.splitext(file_name)[1].lower()
        if ext not in AUDIO_EXTENSIONS:
            continue

        # Output file path
        output_file = os.path.splitext(file_name)[0] + "_128kbps.mp3"
        output_path = os.path.join(output_folder, output_file)

        # Convert
        print(f"Converting: {file_name} → {output_file}")
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="mp3", bitrate="128k")

    print("\n✔ All files converted!")
    print(f"Saved in: {output_folder}")


# ----------- RUN -------------
if __name__ == "__main__":
    folder = "/home/jo/Desktop/LookingforLove"  # <--- CHANGE THIS
    convert_folder_to_128kbps(folder)

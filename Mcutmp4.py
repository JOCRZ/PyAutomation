from moviepy.editor import VideoFileClip, concatenate_videoclips

# Input and output paths
input_path = "input.mp4"
output_path = "final_output.mp4"

# --- Option 1: Define timestamps manually ---
timestamps = [
    ("00:17:39", "00:22:02"),
    ("00:22:53", "00:28:08"),
    ("00:58:07", "01:02:33")
]

# --- Option 2: Read from timestamps.txt if it exists ---
try:
    with open("timestamps.txt") as f:
        timestamps = []
        for line in f:
            if line.strip():
                start, end = line.strip().split(',')
                timestamps.append((start.strip(), end.strip()))
except FileNotFoundError:
    print("No timestamps.txt found, using hardcoded timestamps.")

# --- Load main video ---
video = VideoFileClip(input_path)

# --- Cut each segment ---
clips = []
for start, end in timestamps:
    print(f"Cutting from {start} to {end}...")
    clips.append(video.subclip(start, end))

# --- Merge all clips together ---
final_clip = concatenate_videoclips(clips)

# --- Export merged video ---
final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

print("✅ Done! Saved as", output_path)


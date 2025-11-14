from moviepy.editor import VideoFileClip

# Input video
input_path = "input3.mp4"
output_path = "HND-765.mp4"

# Example timestamps (in seconds)
start_time = "00:53:50"    # 00:00:30
end_time = "02:42:34"    # 00:01:30

# Load video and trim
clip = VideoFileClip(input_path).subclip(start_time, end_time)

# Export result
clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

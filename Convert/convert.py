from moviepy.editor import *

def mp4_to_mp3(input_folder, output_folder):
    """Converts all MP4 files in an input folder to MP3 files in an output folder.

    Args:
        input_folder (str): The path to the input folder containing MP4 files.
        output_folder (str): The path to the output folder where MP3 files will be saved.
    """

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename[:-4] + ".mp3")

            video = VideoFileClip(input_path)
            audio = video.audio
            audio.write_audiofile(output_path)
            audio.close()

if __name__ == "__main__":
    input_folder = "/home/jo/Downloads/VideSeparater/mp4"
    output_folder = "/home/jo/Downloads/VideSeparater/mp3"

    mp4_to_mp3(input_folder, output_folder)

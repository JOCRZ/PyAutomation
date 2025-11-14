import yt_dlp
import os

# -----------------------------
# ENTER YOUR PLAYLIST URL HERE
# -----------------------------
PLAYLIST_URL = "https://www.youtube.com/watch?v=AcMBnffhtJk&list=PLhqFf5_6vY4xLXL9CyXX_EGHQ2ileyMXO"

def download_playlist_mp3(url):
    # Step 1: Extract playlist info (title + entries)
    extract_opts = {
        'quiet': True,
        'extract_flat': False,
    }

    with yt_dlp.YoutubeDL(extract_opts) as ydl:
        playlist_info = ydl.extract_info(url, download=False)

    # Playlist title → folder
    playlist_title = playlist_info.get("title", "playlist").replace("/", "_")
    print(f"Playlist Title: {playlist_title}")

    # Create folder
    if not os.path.exists(playlist_title):
        os.makedirs(playlist_title)

    # Get videos in playlist order
    entries = playlist_info["entries"]

    # REVERSE playlist order for numbering
    entries_reversed = list(reversed(entries))

    ydl_opts = {
        "format": "bestaudio/best",
        "extractaudio": True,
        "audioformat": "mp3",
        "audioquality": "0",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        "outtmpl": {"default": ""}  # temporary placeholder
    }

    # Step 3: Download in reverse order
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        total = len(entries_reversed)
        digits = len(str(total))  # for 01, 02, 03...

        for index, video in enumerate(entries_reversed, start=1):
            num = str(index).zfill(digits)
            title = video.get("title", "audio").replace("/", "_")

            filename = f"{num} - {title}.%(ext)s"
            output_path = os.path.join(playlist_title, filename)

            print(f"Downloading (reverse order): {num} - {title}")

            ydl.params["outtmpl"] = {"default": output_path}

            ydl.download([video["webpage_url"]])

    print("\nAll MP3 files downloaded in reverse-order numbering!")

# Run
download_playlist_mp3(PLAYLIST_URL)

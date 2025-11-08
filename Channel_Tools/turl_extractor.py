import csv
from yt_dlp import YoutubeDL

playlist_url = 'https://www.youtube.com/watch?v=DKi6uhUYHtQ&list=PLGQiSf7MYlFkwwqZQ1buM4kJPSPV5g-V6'

with open("playlist_videos.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["num", "url"])

    ydl_opts = {'ignoreerrors': True}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        entries = info_dict.get("entries", [])
        for entry in entries:
            if entry:
                writer.writerow([entry.get("title", ""), entry.get("webpage_url", "")])



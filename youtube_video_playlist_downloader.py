from pytubefix import Playlist
from pytubefix.cli import on_progress


try:
    url = input("Enter the url: ")

    pl = Playlist(url)

    for index, video in enumerate(pl.videos, start=1):
        file_name = str(index) + "-" + video.title + ".mp4"
        ys = video.streams.get_highest_resolution()
        print(f"Dowloading :{file_name}\n")
        ys.download(output_path="YouTube_playlist", filename=file_name)
    
    print("\nSuccessfully Downloaded all videos")

except Exception as e:
    print("Error occured:", e)
    

from pytubefix import YouTube
from pytubefix.cli import on_progress

file_no = 1
while True:
    url = input("Enter your YouTube video URL (or type 'exit' to stop): ")
    if url.lower() == "exit" or url == "0":
        print("\nDownload session ended.")
        break

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        file_name = str(file_no) + "-" + yt.title + ".mp4"
        ys = yt.streams.get_highest_resolution()
        print(f"Downloading {file_name}")
        ys.download(output_path="YouTube_videos", filename=file_name)
        print("Download completed succesfully")
        file_no += 1
    
    except Exception as e:
        print("Error:", e)

    
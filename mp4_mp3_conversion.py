import subprocess
import os

files = os.listdir('YouTube_playlist') 
# files = os.listdir('YouTube_video') if you have downloade youtube video one by one, not a playlist
os.makedirs("audio", exist_ok=True)
try:
    for file in files:
        video_no = file.split('-')[0]
        video_name = file.split('-')[1:]
        video_name = ",".join(video_name)[:-4]
        subprocess.run(["ffmpeg", "-i", f"YouTube_playlist/{file}", f"audio/{video_no}_{video_name}.mp3"])
        # subprocess.run(["ffmpeg", "-i", f"Youtube_video/{file}", f"audio/{video_no}_{video_name}.mp3"]) same here 'youtube_video'

    print("mp4 to mp3 conversion completed")
except Exception as e:
    print("Error occured:", e)
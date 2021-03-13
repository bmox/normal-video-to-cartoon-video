#link demo https://youtu.be/OkXttCJFL5g
import os
def youtube_downloader(youtube_id, youtube_quality, quality_number=137):
    if youtube_quality=="Auto":
            dummy="youtube-dl --format mp4 https://www.youtube.com/watch?v="+youtube_id[-1]
            try:
              os.system(dummy)
              print("Download successful")
            except:
              print("Can't download")
    elif youtube_quality=="Manual":
      dummy=f"youtube-dl  https://youtu.be/{youtube_id[-1]} -f {quality_number}+bestaudio"
      try:
        os.system(dummy)
        print("Download successful")
      except:
        print("Can't download")

#link demo https://youtu.be/OkXttCJFL5g
import os
from glob import glob
import datetime
def youtube_downloader(my_parameter):
    enter_youtube_link = my_parameter[0]
    youtube_quality = my_parameter[1]
    quality_number = my_parameter[2]
    select_duration = my_parameter[3]
    enter_start_time = my_parameter[4]
    enter_end_time = my_parameter[5]
    youtube_id = enter_youtube_link.split("/")

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
    start_time_float = enter_start_time.split(":")
    end_time_float = enter_end_time.split(":")
    start_time_in_second = (float(start_time_float[0]) * 60 * 60) + (float(start_time_float[1]) * 60) + float(
        start_time_float[2])
    end_time_in_second = (float(end_time_float[0]) * 60 * 60) + (float(end_time_float[1]) * 60) + float(
        end_time_float[2])
    cut_time_duration = end_time_in_second - start_time_in_second
    cut_time = str(datetime.timedelta(seconds=cut_time_duration))
    return enter_start_time,select_duration,cut_time


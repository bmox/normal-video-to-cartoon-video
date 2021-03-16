from youtube_video_downloader import youtube_downloader
# !python test.py https://youtu.be/eAmGbA0JyIU,Auto,137,full_video,00:00:00,00:00:60,yes
import sys
import os
from glob import glob
import datetime
argu=str(sys.argv[1])
my_parameter=argu.split(",")

delete_video = []
extensions = ['/*.mp4', '/*.mkv']
for ext in extensions:
    delete_video.extend(glob(os.getcwd()+ext))
print(delete_video)
for i in delete_video:
  try:
    os.remove(i)
    print("Delete old video")
  except:
    pass
enter_youtube_link = my_parameter[0]
youtube_quality = my_parameter[1]
quality_number = my_parameter[2]
select_duration = my_parameter[3]
enter_start_time = my_parameter[4]
enter_end_time = my_parameter[5]
youtube_downloader(enter_youtube_link,youtube_quality,quality_number)

def trim(enter_start_time,enter_end_time,select_duration):
  start_time_float = enter_start_time.split(":")
  end_time_float = enter_end_time.split(":")
  start_time_in_second = (float(start_time_float[0]) * 60 * 60) + (float(start_time_float[1]) * 60) + float(
      start_time_float[2])
  end_time_in_second = (float(end_time_float[0]) * 60 * 60) + (float(end_time_float[1]) * 60) + float(
      end_time_float[2])
  files = []
  extensions = ['/*.mp4', '/*.mkv']
  for ext in extensions:
      files.extend(glob(os.getcwd()+ext))
  print(files)
  extensions = ['/*.mp4', '/*.mkv']
  for ext in extensions:
      files.extend(glob(os.getcwd()+ext))
  print(files)
  dummy_extenstion=""
  if files[0].endswith(".mp4"):
      dummy_extenstion=".mp4"
  elif files[0].endswith(".mkv"):
      dummy_extenstion=".mkv"
  if select_duration == "full_video":
      pass
  elif select_duration == "some_part":
      cut_time_duration = end_time_in_second - start_time_in_second
      cut_time = str(datetime.timedelta(seconds=cut_time_duration))
      print("Trim video")
      cut_command = f"ffmpeg -ss {enter_start_time} -i '{files[0]}' -t {cut_time} -c copy 'cut{dummy_extenstion}'"
      print(cut_command)
      var7=os.system(cut_command)
      print(var7)
      os.remove(files[0])
      os.rename(f"cut{dummy_extenstion}", files[0])
trim(enter_start_time,enter_end_time,select_duration)
print(my_parameter[-1])


# print(my_parameter[-1])




image_extenstion="png"#@param ["jpg","png"]
frames_image = []

from os.path import join
import shutil

try:
   os.remove("input_video.mp4")
except:
   pass
try:
    os.mkdir("test_images")
except:
    pass
test_image=[]
if len(glob(f"./test_images/*.{image_extenstion}"))!=0:
    for i in glob(f"./test_images/*.{image_extenstion}"):
        test_image.append(i)
    for i in test_image:
       os.remove(i)
else:
    pass
try:
    os.mkdir("cartoonized_images")
except:
    pass
try:
   if len(glob(f"./cartoonized_images/*.{image_extenstion}")) != 0:
       cartoonized_images = []
       for i in glob(f"./cartoonized_images/*.{image_extenstion}"):
          cartoonized_images.append(i)
       for i in cartoonized_images:
          os.remove(i)
   else:
       pass
except Exception as e:
   print(str(e))

files = []
extensions = ['*.mp4', '*.mkv']
for ext in extensions:
   files.extend(glob(join("", ext)))

print(files)
video_title=files[0]
if files[0].endswith(".mp4"):
   os.rename(files[0],"input_video.mp4")
elif files[0].endswith(".mkv"):
   os.rename(files[0],"input_video.mkv")
try:
   var=os.system(f'ffmpeg -i "./input_video.mp4" "test_images/%03d.{image_extenstion}"')
   if var==0:
      print("Frame extract successful")
   else:
      print("Can't extract any frame")
except Exception as e:
   print(str(e))

root_path=os.getcwd()
var1=os.system("python cartoonize.py")
if var1==0:
   print("cartoonized complete")
else:
   print("cartoonize failed")

 #upscale image
if my_parameter[-1]=="yes":
   print("Upscaling")
   os.system("python upscale.py")
elif my_parameter[-1]=="no":
   print("No upscaling")
else:
   pass
   
   
os.chdir("./cartoonized_images")
#print(os.getcwd())
var3=os.system(f"ffmpeg -framerate 30 -i %03d.{image_extenstion} cartoon.mp4")
if var3==0:
    print("We successfully make the cartoonized video.")
else:
    print("We can't make the cartoonized video.")
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
#print(os.getcwd())
try:
    os.mkdir("input_video")
except:
    pass
remove_list=["./input_video/input_video.mp4","./input_video/cartoon.mp4"]
for i in remove_list:
      try:
         os.remove(i)
      except:
         pass

shutil.move("input_video.mp4","./input_video/")
shutil.move("./cartoonized_images/cartoon.mp4","./input_video/")


os.chdir("./input_video")
if video_title.endswith(".mp4"):
    extension=".mp4"
elif video_title.endswith(".mkv"):
    extension = ".mkv"

var4=os.system(f"ffmpeg -i input_video{extension} audio.wav")
if var4==0:
    print("Successfully export audio")
else:
    print("Failed to export audio")
var5=os.system(f"ffmpeg -i cartoon.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 cartoon_audio.mp4")
if var5==0:
    print("Successfully replace audio in output file")
else:
    print("Failed to replace audio in output file")
path_parent1 = os.path.dirname(os.getcwd())
os.chdir(path_parent1)

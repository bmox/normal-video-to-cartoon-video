from glob import glob
# li=[]
# for i in glob("cartoonized_images/*.jpg"):
#     print(i)
#     li.append(i)
# print(len(li))
import os
import shutil
os.chdir("./cartoonized_images")
print(os.getcwd())
var3=os.system("ffmpeg -framerate 24 -i out-%03d.jpg cartoon.mp4")
if var3==0:
    print("We successfully make the cartoonized video.")
else:
    print("We can't make the cartoonized video.")
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print(os.getcwd())
try:
    os.mkdir("input_video")
except:
    pass
shutil.move("input_video.mp4","./input_video/")
shutil.move("./cartoonized_images/cartoon.mp4","./input_video/")



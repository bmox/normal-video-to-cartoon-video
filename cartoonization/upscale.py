
import os
from glob import glob
import shutil
# try:
#   os.chdir(root_path)
# except:
#   pass

image_extenstion="png"#["jpg","png"]
# print(os.getcwd())
full_path=os.getcwd()
low_cartoon=[]
for i in glob(f"{full_path}/cartoonized_images/*.{image_extenstion}"):
  low_cartoon.append(i)

os.chdir("./waifu2x-chainer-master")
for i in glob(f"./*.{image_extenstion}"):
  try:
    os.remove(i)
  except:
    pass


for i in low_cartoon:
  var5=os.system(f"python waifu2x.py --method noise_scale --noise_level 1 --input '{i}' --arch VGG7 --gpu 0")

for i in low_cartoon:
  os.remove(i)

high_cartoon=[]
for i in low_cartoon:
  high_cartoon.append(i.split("/")[-1])

move_path=full_path+"/cartoonized_images/"
for i in high_cartoon:
  shutil.move(i,move_path)

path_parent1 = os.path.dirname(os.getcwd())
os.chdir(path_parent1)

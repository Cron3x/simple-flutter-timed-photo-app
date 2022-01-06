from PIL import Image
from PIL.ExifTags import TAGS

import glob, os
os.chdir("Photos/")
try:
    os.mkdir("conv/")
except OSError as e:
    print(e)

dates_list = []

for file in glob.glob("*.jpg"):
    # path to the image or video
    imagename = file

    # read the image data using PIL
    image = Image.open(imagename)

    # extract EXIF data
    exifdata = image.getexif()
    mod_exif = exifdata[306].split(' ')[0].replace(':','+')
    print(f"{mod_exif}.jpg")
    image.save(f"conv/{mod_exif}.jpg")
    dates_list.append(mod_exif)


dates_list.sort()
print(dates_list)

for i in range(len(dates_list)):
    os.rename(f"conv/{dates_list[i]}.jpg", f"conv/{i}.jpg")

os.system('ffmpeg -start_number 0 -i "conv/%d.jpg" -c:v libx264 -vf "fps=30,format=yuv420p" out.mp4')

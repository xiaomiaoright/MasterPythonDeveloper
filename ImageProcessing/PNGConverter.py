
# import packages
import sys
import os
from PIL import Image

# use sys grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# check if new folder exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print('Created')
# loop through folder and convert images to png
for filename in os.listdir(image_folder):
    # fileName2 = (filename.split(".")[0])
    fileName2 = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{fileName2}.png','png')
    print(filename)


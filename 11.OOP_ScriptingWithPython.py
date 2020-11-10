# Image Processing
from PIL import Image, ImageFilter

img = Image.open(r'ImageProcessing\ImageDataset\Cat.jpg')
img.size
img.format


filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save(r'ImageProcessing\ImageDataset\CatBlurred.png', 'png')

grey_image = img.convert('L')
grey_image.save(r'ImageProcessing\ImageDataset\CatGrey.png', 'png')

grey_image.show()

img.rotate(90)

resize_image = img.resize((300,300))
resize_image.save(r'ImageProcessing\ImageDataset\Catresize.png', 'png')


box = (100,100,200,200)
image_region = img.crop(box)
image_region.show()


# Resize Keep aspect ratio
img.thumbnail((400,200))
img.show()

# create a jpg to png converter
# imput folder path 
# convert all images in the folder to png
# create a new folder and save the converted image


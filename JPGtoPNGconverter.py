#convert the given folder jpg images to png images. As png images have lot of benefits. 
# sample syntax in terminal - > python JPGtoPNGconverter.py pokedex\ new\
import sys
import os
from os import listdir
from PIL import Image, ImageFilter #this is from pip install pillow used for image processing.

#grab the current and new folder images
path = sys.argv[1]  #pokedex\

directory = sys.argv[2] #new\
print(path, directory)

#if new folder doesn't exist, create one
if not os.path.exists(directory):
    os.makedirs(directory)

#figruing out github
#loop through pokedex - current folder

for images in os.listdir(path):
    if(images.endswith('.jpg')):

        imgtoconvert = Image.open(f'{path}{images}')
        imgname = images.split('.')[0]
        imgtoconvert.save(f'{directory}{imgname}.png','png')
        
print('all done!')

#convert images from jpg to png
#save to the new folder. 



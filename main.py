"""
@author: dargor980
"""

import genericpath
from PIL import Image
import PIL.ImageOps
import time
import os

def negativeToColorImage(im):
    initTime = time.time()
    path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/') + im 
    im = Image.open(path)
    im.show()
    imAux = im
    i = 0
    while i < imAux.size[0]:
        j = 0
        while j < imAux.size[1]:
            r, g, b = imAux.getpixel((i,j))
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b 
            pixel = tuple([rn, gn, bn])
            imAux.putpixel((i,j), pixel)
            j+=1
        i+=1
    imAux.show()
    finishTime = time.time()
    print("Time elapsed: ", finishTime - initTime, 'seconds.')


def bAndGNegativeToImage(im):
    initTime = time.time()
    path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop/') + im
    im = Image.open(path)
    finalImage = PIL.ImageOps.invert(im)
    finalImage.show()


im = input("Ingrese el nombre del archivo (debe incluir extensión): ")
bAndGNegativeToImage(im)

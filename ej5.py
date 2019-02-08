#ej5.py
#Por Luis Diego Fernandez
import sys
import math
import bmp_maker

# image attributes
width = 800
height = 600
x_to_paint = 1
y_to_paint = 1
bits_per_pixel = 32

newBmpImage = bmp_maker.bmpImage()
newBmpImage.glCreateWindow(width, height)
newBmpImage.glClearColor(0,0,0)
newBmpImage.glColor(1,1,1);
newBmpImage.glClear()

newBmpImage.glLine(-0.75,-0.667,-0.5,-0.667)
newBmpImage.glLine(-0.75,-0.667,-0.75,-0.333)
newBmpImage.glLine(-0.5,-0.667,-0.5,-0.333)
newBmpImage.glLine(-0.75,-0.333,-0.5,-0.333)

newBmpImage.glLine(-0.625,-0.5,-0.375,-0.5)
newBmpImage.glLine(-0.625,-0.5,-0.625,-0.1667)
newBmpImage.glLine(-0.375,-0.5,-0.375,-0.1667)
newBmpImage.glLine(-0.625,-0.1667,-0.375,-0.1667)

newBmpImage.glLine(-0.75,-0.6667,-0.625,-0.5)
newBmpImage.glLine(-0.75,-0.3333,-0.625,-0.1667)
newBmpImage.glLine(-0.5,-0.6667,-0.375,-0.5)
newBmpImage.glLine(-0.5,-0.3333,-0.375,-0.1667)

newBmpImage.glFinishWN("ej5.bmp")

print("Done")

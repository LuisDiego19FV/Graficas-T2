#ejNES.py
#Por Luis Diego Fernandez
import sys
import math
import bmp_maker

# image attributes
width = 32
height = 32
x_to_paint = 1
y_to_paint = 1
bits_per_pixel = 32

# header
newBmpImage = bmp_maker.bmpImage()
newBmpImage.glCreateWindow(width, height)
newBmpImage.glClearColor(1,1,1)
newBmpImage.glClear()

# hat
newBmpImage.glColor(0.76,0.208,0.176)
newBmpImage.glLine(-0.25,1,0.375,1)
newBmpImage.glLine(-0.25,0.9375,0.375,0.9375)
newBmpImage.glLine(-0.375,0.875,0.75,0.875)
newBmpImage.glLine(-0.375,0.8125,0.75,0.8125)

# face 1
newBmpImage.glColor(0.510,0.298,0.255)
newBmpImage.glLine(-0.375,0.75,-0.0625,0.75)
newBmpImage.glLine(-0.375,0.6875,-0.0625,0.6875)
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(0,0.75,0.25,0.75)
newBmpImage.glLine(0,0.6875,0.25,0.6875)
newBmpImage.glColor(0,0,0)
newBmpImage.glLine(0.3125,0.75,0.375,0.75)
newBmpImage.glLine(0.3125,0.6875,0.375,0.6875)
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(0.4375,0.75,0.5,0.75)
newBmpImage.glLine(0.4375,0.6875,0.5,0.6875)

# face 2
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(-0.125,0.625,0.25,0.625)
newBmpImage.glLine(-0.125,0.5625,0.25,0.5625)
newBmpImage.glLine(-0.375,0.625,-0.3125,0.625)
newBmpImage.glLine(-0.375,0.5625,-0.3125,0.5625)
newBmpImage.glColor(0,0,0)
newBmpImage.glLine(0.3125,0.625,0.375,0.625)
newBmpImage.glLine(0.3125,0.5625,0.375,0.5625)
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(0.4375,0.625,0.75,0.625)
newBmpImage.glLine(0.4375,0.5625,0.75,0.5625)
newBmpImage.glColor(0.510,0.298,0.255)
newBmpImage.glLine(-0.25,0.625,-0.1875,0.625)
newBmpImage.glLine(-0.25,0.5625,-0.1875,0.5625)
newBmpImage.glLine(-0.5,0.625,-0.4375,0.625)
newBmpImage.glLine(-0.5,0.5625,-0.4375,0.5625)

# face 3
newBmpImage.glColor(0.510,0.298,0.255)
newBmpImage.glLine(-0.5,0.5,-0.0625,0.5)
newBmpImage.glLine(-0.5,0.4375,-0.0625,0.4375)
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(0,0.5,0.875,0.5)
newBmpImage.glLine(0,0.4375,0.875,0.4375)
newBmpImage.glLine(-0.375,0.5,-0.3125,0.5)
newBmpImage.glLine(-0.375,0.4375,-0.3125,0.4375)
newBmpImage.glColor(0,0,0)
newBmpImage.glLine(0.4375,0.5,0.5,0.5)
newBmpImage.glLine(0.4375,0.4375,0.5,0.4375)

# face 4
newBmpImage.glColor(0.510,0.298,0.255)
newBmpImage.glLine(-0.375,0.375,-0.0625,0.375)
newBmpImage.glLine(-0.375,0.3125,-0.0625,0.3125)
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(-0.25,0.375,0.25,0.375)
newBmpImage.glLine(-0.25,0.3125,0.25,0.3125)
newBmpImage.glColor(0,0,0)
newBmpImage.glLine(0.3125,0.375,0.75,0.375)
newBmpImage.glLine(0.3125,0.3125,0.75,0.3125)

# face 5
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(-0.25,0.25,0.5,0.25)
newBmpImage.glLine(-0.25,0.1865,0.5,0.1865)

# body skin 1
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(0,0.6875,0.25,0.6875)
newBmpImage.glLine(-0.625,-0.25,0.875,-0.25)
newBmpImage.glLine(-0.625,-0.3125,0.875,-0.3125)
newBmpImage.glLine(-0.625,-0.375,0.875,-0.375)
newBmpImage.glLine(-0.625,-0.4375,0.875,-0.4375)
newBmpImage.glLine(-0.625,-0.5,0.875,-0.5)
newBmpImage.glLine(-0.625,-0.5625,0.875,-0.5625)

# body blue
newBmpImage.glColor(0.231,0.275,0.820)
newBmpImage.glLine(-0.375,0.125,0.375,0.125)
newBmpImage.glLine(-0.375,0.0625,0.375,0.0625)
newBmpImage.glLine(-0.5,0.0,0.75,0.0)
newBmpImage.glLine(-0.5,-0.0625,0.75,-0.0625)
newBmpImage.glLine(-0.625,-0.125,0.875,-0.125)
newBmpImage.glLine(-0.625,-0.1875,0.875,-0.1875)
newBmpImage.glLine(-0.625,-0.25,0.875,-0.25)
newBmpImage.glLine(-0.625,-0.3125,0.875,-0.3125)

#boby skin 2
newBmpImage.glColor(0.947,0.721,0.527)
newBmpImage.glLine(-0.625,-0.3125,-0.4375,-0.3125)
newBmpImage.glLine(-0.625,-0.25,-0.4375,-0.25)
newBmpImage.glLine(0.6875,-0.3125,0.875,-0.3125)
newBmpImage.glLine(0.6875,-0.25,0.875,-0.25)

# body red
newBmpImage.glColor(0.76,0.208,0.176)
newBmpImage.glLine(-0.125,0.125,-0.0625,0.125)
newBmpImage.glLine(-0.125,0.0625,-0.0625,0.0625)
newBmpImage.glLine(-0.125,0,-0.0625,0)
newBmpImage.glLine(-0.125,-0.0625,-0.0625,-0.0625)
newBmpImage.glLine(-0.125,-0.125,-0.0625,-0.125)
newBmpImage.glLine(-0.125,-0.1875,-0.0625,-0.1875)
newBmpImage.glLine(-0.125,-0.25,0.375,-0.25)
newBmpImage.glLine(-0.125,-0.3125,0.375,-0.3125)
newBmpImage.glLine(0.3125,0.125,0.375,0.125)
newBmpImage.glLine(0.3125,0.0625,0.375,0.0625)
newBmpImage.glLine(0.3125,0,0.375,0)
newBmpImage.glLine(0.3125,-0.0625,0.375,-0.0625)
newBmpImage.glLine(0.3125,-0.125,0.375,-0.125)
newBmpImage.glLine(0.3125,-0.1875,0.375,-0.1875)
newBmpImage.glLine(-0.125,-0.25,0.375,-0.25)
newBmpImage.glLine(-0.125,-0.3125,0.375,-0.3125)
newBmpImage.glLine(-0.25,-0.375,0.5,-0.375)
newBmpImage.glLine(-0.25,-0.4375,0.5,-0.4375)
newBmpImage.glLine(-0.375,-0.5,0.625,-0.5)
newBmpImage.glLine(-0.375,-0.5625,0.625,-0.5625)
newBmpImage.glLine(-0.375,-0.625,0.0,-0.625)
newBmpImage.glLine(-0.375,-0.6875,0.0,-0.6875)
newBmpImage.glLine(0.25,-0.625,0.625,-0.625)
newBmpImage.glLine(0.25,-0.6875,0.625,-0.6875)

# boots
newBmpImage.glColor(0.510,0.298,0.255)
newBmpImage.glLine(-0.5,-0.75,-0.125,-0.75)
newBmpImage.glLine(-0.5,-0.8125,-0.125,-0.8125)
newBmpImage.glLine(0.375,-0.75,0.75,-0.75)
newBmpImage.glLine(0.375,-0.8125,0.75,-0.8125)
newBmpImage.glLine(-0.625,-0.875,-0.125,-0.875)
newBmpImage.glLine(-0.625,-0.9375,-0.125,-0.9375)
newBmpImage.glLine(0.375,-0.875,0.875,-0.875)
newBmpImage.glLine(0.375,-0.9375,0.875,-0.9375)

# buttons
newBmpImage.glColor(1,0.8,0)
newBmpImage.glLine(-0.125,-0.375,-0.0625,-0.375)
newBmpImage.glLine(-0.125,-0.4375,-0.0625,-0.4375)
newBmpImage.glLine(0.3125,-0.375,0.375,-0.375)
newBmpImage.glLine(0.3125,-0.4375,0.375,-0.4375)

# write image
newBmpImage.glFinishWN("ejNES.bmp")

print("Done")

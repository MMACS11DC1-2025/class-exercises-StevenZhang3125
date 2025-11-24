import time

t0 = time.time()

from PIL import Image

imageIn = Image.open("5.4/jelly_beans.jpg")
pixels = imageIn.load()

width = imageIn.width
height = imageIn.height
yelllowPixels = 0
redPixels = 0

t1 = time.time()

for i in range(width):
    for k in range(height):
        r = pixels[i, k][0]
        g = pixels[i, k][1]
        b = pixels[i, k][2]

        if r > 175 and g > 175 and b < 50:
            yelllowPixels+=1

t2 = time.time()

yellowPercentage = (yelllowPixels/(width*height))*100
print(str(yellowPercentage) + "%")
tn0 = time.time() - t0
tn1 = t1 - t0
tn2 = t2 - t1
print("Time Taken for entire program: {:.2f}s; Time Taken for loaded variables: {:.2f}s; Time Taken for : {:.2f}s".format(tn0, tn1, tn2))
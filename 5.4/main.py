from PIL import Image

imageIn = Image.open("5.4/jelly_beans.jpg")
pixels = imageIn.load()

width = imageIn.width
height = imageIn.height
yelllowPixels = 0
redPixels = 0

for i in range(width):
    for k in range(height):
        r = pixels[i, k][0]
        g = pixels[i, k][1]
        b = pixels[i, k][2]

        if r > 175 and g > 175 and b < 50:
            yelllowPixels+=1

yellowPercentage = (yelllowPixels/(width*height))*100
print(str(yellowPercentage) + "%")
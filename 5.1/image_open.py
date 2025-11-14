from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

def is_green(r,g,b):
    if r >= 0 and r < 25 and g > 50 and g <= 255 and  b>= 0 and b < 25:
        return True
    return False

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for k in range(height):
        r = image_green[i, k][0]
        g = image_green[i, k][1]
        b = image_green[i, k][2]

        if is_green(r, g, b):
            image_output.putpixel((i, k), image_beach[i, k])

image_output.save("output.png", "png")
        
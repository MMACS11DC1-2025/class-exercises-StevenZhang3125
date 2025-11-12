from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

def is_green(r,g,b):
    if r >= 0 and r < 25 and g > 230 and g <= 255 and  b>= 0 and b < 25:
        return True
    return False

print(is_green(image_green[0, 0][0],image_green[0, 0][1],image_green[0, 0][2]))
        
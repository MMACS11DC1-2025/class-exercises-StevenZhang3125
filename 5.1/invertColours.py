from PIL import Image

def invert(dir):
    image = Image.open(dir)
    pixels = image.load()

    width = image.width
    height = image.height

    for i in range(width):
        for k in range(height):
            r = pixels[i, k][0]
            g = pixels[i, k][1]
            b = pixels[i, k][2]
            pixels[i, k] = (255-r,255-g,255-b)
    image.save("output.png", "png")
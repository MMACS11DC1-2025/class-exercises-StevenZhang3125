from PIL import Image

def colourInterest(file):
    grayScale = [] # Gray (Colour consistancy; Full white/black could affect data)
    w = file.width
    h = file.height
    pixels = file.load()
    stepW = w//100
    stepH = h//100
    if stepW == 0:
        stepW = 1
    if stepH == 0:
        stepH = 1
    for col in range(0, w, stepW):
        for row in range(0, h, stepH):
            r, g, b = pixels[col,row]
            avg = (r+g+b)//3
            if avg > 200 or avg < 50:
                continue
            avgRange = (avg-2, avg+2)
            if avgRange[0] < r and r < avgRange[1] and avgRange[0] < g and g < avgRange[1] and avgRange[0] < b and b < avgRange[1]:
                grayScale.append(avg)
    avgGray = sum(grayScale)//len(grayScale)
    return avgGray

def otherColours(file, avgGray):
    blacklist = []
    w = file.width
    h = file.height
    pixels = file.load()
    stepW = w//100
    stepH = h//100
    if stepW == 0:
        stepW = 1
    if stepH == 0:
        stepH = 1
    # for col in range(0, w, stepW):
    #     for row in range(0, h, stepH):
    #         r, g, b = pixels[col,row]
    #         avg = (r+g+b)//3
    #         if avg > 200 or avg < 50:
    #             continue
    #         avgRange = (avg-2, avg+2)
    #         if avgRange[0] < r and r < avgRange[1] and avgRange[0] < g and g < avgRange[1] and avgRange[0] < b and b < avgRange[1]:
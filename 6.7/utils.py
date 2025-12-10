from PIL import Image
import math

index = {
    2400: (35, 10, 45),
    2300: (65, 20, 75),
    2200: (95, 25, 85),
    2100: (130, 30, 80),
    2000: (165, 40, 70),
    1900: (200, 55, 55),
    1800: (225, 85, 40),
    1700: (240, 115, 30),
    1600: (250, 145, 25),
    1500: (255, 175, 40),
    1400: (250, 210, 60),
    1300: (235, 235, 90),
    1200: (190, 235, 120),
    1100: (150, 220, 150),
    1000: (110, 205, 175),
    900: (80, 185, 195),
    800: (65, 155, 205),
    700: (60, 120, 195),
    600: (55, 90, 180)
}

def getClosestValue(pixel_color):
    r,g,b = pixel_color
    lowestDiff = math.inf
    for i in range(600, 2500, 100):
        redDiff = abs(r - index[i][0])
        greenDiff = abs(g - index[i][1])
        blueDiff = abs(b - index[i][2])
        totalDiff = redDiff + greenDiff + blueDiff
        if totalDiff < lowestDiff:
            lowestDiff = totalDiff
            closestValue = i
    return closestValue

def isGrayScale(colour):
    r, g, b = colour
    avg = (r + g + b) / 3
    if abs(r - avg) < 10 and abs(g - avg) < 10 and abs(b - avg) < 10:
        return True
    return False

def colourToValue(file):
    pixels = file.load()
    w = file.width
    h = file.height
    values = []
    for r in range(h):
        for c in range(w):
            colour = pixels[c, r]
            if not isGrayScale(colour):
                value = getClosestValue(colour)
                values.append(value)
    return values

def datasetConsistency(data):
    instances = []
    for i in range(600, 2500, 100):
        instances.append(data.count(i))
    return max(instances)/sum(instances)*100

def nestedDatasetSelectionSort(data, index):
    for i in range(len(data)):
        minIndex = i
        for k in range(i+1, len(data)):
            if data[k][index] < data[minIndex][index]:
                minIndex = k
        data[i], data[minIndex] = data[minIndex], data[i]
    return data
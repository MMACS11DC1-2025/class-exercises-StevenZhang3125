from PIL import Image
import math

# Find Gray colour
def colourInterest(file):
    grayScale = [] # Gray (Colour consistancy)
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

# Find other colours (cars, medians); rturn 
def otherColours(file, avgGray):
    blacklistRaw = []
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
    for col in range(0, w, stepW):
        for row in range(0, h, stepH):
            r, g, b = pixels[col,row]
            avgRange = (avgGray-2, avgGray+2)
            isGray = avgRange[0] < r and r < avgRange[1] and avgRange[0] < g and g < avgRange[1] and avgRange[0] < b and b < avgRange[1]
            if not isGray:
                blacklistRaw.append(bfs(file, (col, row), (r, g, b)))
                for i in range(len(blacklistRaw)):
                    minXArray, maxXArray = nestedMinMaxFinder(blacklistRaw[i], 0)
                    minX, maxX = minXArray[0], maxXArray[1]
                    minYArray, maxYArray = nestedMinMaxFinder(blacklistRaw[i], 1)
                    minY, maxY = minYArray[0], maxYArray[1]
                    blacklist.append((minX, maxX, minY, maxY))
    return blacklist
    
# Breadth First Search to find clumps of colours
def bfs(file, start, colours):
    visited = []
    queue = [start]
    w = file.width
    h = file.height
    pixels = file.load()
    while queue:
        col, row = queue.pop(0)
        if (col, row) in visited:
            continue
        visited.add((col, row))
        r, g, b = pixels[col, row]
        colourRange = [(colours[0]-10, colours[0]+10), (colours[1]-10, colours[1]+10), (colours[2]-10, colours[2]+10)]
        inRange = colourRange[0][0] < r and r < colourRange[0][1] and colourRange[1][0] < g and g < colourRange[1][1] and colourRange[2][0] < b and b < colourRange[2][1]
        # Left
        if col != 0:
            if inRange:
                queue.append((col-1, row))
        # Right
        if col != w-1:
            if inRange:
                queue.append((col+1, row))
        # Up
        if row != 0:
            if inRange:
                queue.append((col, row-1))
        # Down
        if row != h-1:
            if inRange:
                queue.append((col, row+1))
    return visited

# Find min and max values in a nested array; returns the array with the desired value
def nestedMinMaxFinder(array, index):
    minVal = math.inf
    minArray = []
    maxVal = -math.inf
    maxArray = []
    for i in range(len(array)):
        if array[i][index] < minVal:
            minVal = array[i][index]
            minArray = array[i]
        if array[i][index] > maxVal:
            maxVal = array[i][index]
            maxArray = array[i]
    return minArray, maxArray
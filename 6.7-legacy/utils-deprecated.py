from PIL import Image
import math
from collections import deque

# Find asphalt colour
def colourInterest(file):
    # Initalization
    grayScale = []  # List of all gray colours
    w = file.width
    h = file.height
    pixels = file.load()

    # Check only 100 pixels per row and column
    stepW = w//100
    stepH = h//100

    # Avoid step of 0
    if stepW == 0:
        stepW = 1
    if stepH == 0:
        stepH = 1

    # Interate through pixels (Every 100)
    for col in range(0, w, stepW):
        for row in range(0, h, stepH):
            r, g, b = pixels[col,row]
            avg = (r+g+b)//3          # Gray scale
            if avg > 200 or avg < 50: # Too light or too dark
                continue
            avgRange = (avg-2, avg+2) # Colour tolerance
            if avgRange[0] < r and r < avgRange[1] and avgRange[0] < g and g < avgRange[1] and avgRange[0] < b and b < avgRange[1]: # Is gray
                grayScale.append(avg)
    avgGray = sum(grayScale)//len(grayScale) # Average gray value (Of all gray pixels)
    return avgGray

# Find other colours (cars, medians)
def otherColours(file, avgGray):
    # Initalization
    blacklistRaw = []  # Individual pixel blacklist
    blacklist = []     # Bounding box blacklist
    allVisited = set() # Use set to avoid O(n) lookup
    w = file.width
    h = file.height
    pixels = file.load()

    # Check only 100 pixels per row and column
    stepW = w//100
    stepH = h//100

    # Avoid step of 0
    if stepW == 0:
        stepW = 1
    if stepH == 0:
        stepH = 1

    # Interate through pixels (Every 100)
    for col in range(0, w, stepW):
        for row in range(0, h, stepH):
            if (col, row) in allVisited: # Skip already visited pixels
                continue
            r, g, b = pixels[col,row]
            avgRange = (avgGray-2, avgGray+2) # Colour tolerance
            isGray = avgRange[0] < r and r < avgRange[1] and avgRange[0] < g and g < avgRange[1] and avgRange[0] < b and b < avgRange[1] # Is pixel gray
            if not isGray:                                 # Is pixel not gray (Car/median; not asphalt)
                visited = bfs(file, (col, row), (r, g, b)) # Find neighbouring pixels of same colour
                allVisited.update(visited)                 # Update allVisited set
                blacklistRaw.append(visited)               # Add to blacklist raw
    # Deprecated (maybe)
    # for i in range(len(blacklistRaw)):
    #     minXArray, maxXArray = nestedMinMaxFinder(blacklistRaw[i], 0)
    #     minX, maxX = minXArray[0], maxXArray[1]
    #     minYArray, maxYArray = nestedMinMaxFinder(blacklistRaw[i], 1)
    #     minY, maxY = minYArray[0], maxYArray[1]
    #     blacklist.append((minX, maxX, minY, maxY))
    return blacklistRaw

# Find white lines (Parking lines)
def whiteLinesFinder(file, start, blacklist):
    # Initalization
    whiteLinesRaw = [] # Individual white pixels (excluding cars)
    allVisited = set() # Use set to avoid O(n) lookup
    w = file.width
    h = file.height
    pixels = file.load()

    # Check only 250 pixels per row and column
    stepW = w//250
    stepH = h//250

    # Avoid step of 0
    if stepW == 0:
        stepW = 1
    if stepH == 0:
        stepH = 1

    # Interate through pixels (Every 250)
    for col in range(start[0], w, stepW):
        for row in range(start[1], h, stepH):
            r, g, b = pixels[col,row]
            avgRange = (190, 255) # White colour range/tolerance
            isWhite = avgRange[0] < r and r < avgRange[1] and avgRange[0] < g and g < avgRange[1] and avgRange[0] < b and b < avgRange[1] # Is pixel white
            if isWhite:
                if (col, row) not in allVisited: # Skip already visited pixels
                    if (col, row) in blacklist:  # Skip blacklisted pixels
                        continue
                    visited = bfs(file, (col, row), "white")           # Find neighbouring white pixels (configured to "white" for custom range)
                    allVisited.update(visited)                         # Update allVisited set
                    whiteLinesRaw.append(list(visited))            # Add to whiteLinesRaw
    if not allVisited:                                                 # No white pixels found
        return whiteLinesFinder(file, (stepW//2, stepH//2), blacklist) # Retry with offset start point (half of previous step)
    return whiteLinePartitioner(whiteLinesRaw)                         # Return partitioned white lines (Segments; edges intercept other segments) (Possibly deprecated)

def whiteLinePartitioner(whiteLinesRaw):
    whiteLines = []
    # Implement partitioning logic here (maybe)
    return whiteLinesRaw

# Breadth First Search to find neighbouring pixels of colour range
def bfs(file, start, colours):
    # Initalization
    visited = set()        # Use set to avoid O(n) lookup
    queue = deque([start]) # Use deque to avoid O(n) poping
    w = file.width
    h = file.height
    pixels = file.load()

    # BFS Loop
    while queue:
        col, row = queue.popleft()
        if (col, row) in visited: # Skip already visited pixels
            continue
        visited.add((col, row))   # Mark current pixel as visited
        r, g, b = pixels[col, row]
        if colours == "white":    # Custom white range
            colourRange = [(190, 255), (190, 255), (190, 255)]
        else:
            colourRange = [(colours[0]-10, colours[0]+10), (colours[1]-10, colours[1]+10), (colours[2]-10, colours[2]+10)] # Colour tolerance
        inRange = colourRange[0][0] < r and r < colourRange[0][1] and colourRange[1][0] < g and g < colourRange[1][1] and colourRange[2][0] < b and b < colourRange[2][1] # Is pixel colour in colour range
        # Left
        if col != 0:
            if inRange and not (col-1, row) in visited:
                queue.append((col-1, row))
        # Right
        if col != w-1:
            if inRange and not (col+1, row) in visited:
                queue.append((col+1, row))
        # Up
        if row != 0:
            if inRange and not (col, row-1) in visited:
                queue.append((col, row-1))
        # Down
        if row != h-1:
            if inRange and not (col, row+1) in visited:
                queue.append((col, row+1))
    return list(visited) # Return visited pixels (Clump/area)

# Find min and max values in a nested array; returns the nested array with the desired value
def nestedMinMaxFinder(array, index):
    # Initalization
    minVal = math.inf
    minArray = []
    maxVal = -math.inf
    maxArray = []
    # Find min and max
    for i in range(len(array)):
        if array[i][index] < minVal:
            minVal = array[i][index]
            minArray = array[i]
        if array[i][index] > maxVal:
            maxVal = array[i][index]
            maxArray = array[i]
    return minArray, maxArray
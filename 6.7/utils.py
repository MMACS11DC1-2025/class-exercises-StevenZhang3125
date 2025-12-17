from PIL import Image
import math

# Reference colour to kWh value mapping
colourReference = {
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

# Get closest kWh value based on pixel colour
def getClosestValue(pixel_color):
    r, g, b = pixel_color
    lowestDiff = math.inf
    for value in range(600, 2500, 100): # Iterate through reference values
        # Difference of each colour in a pixel compared to reference colour
        redDiff = abs(r - colourReference[value][0])
        greenDiff = abs(g - colourReference[value][1])
        blueDiff = abs(b - colourReference[value][2])
        totalDiff = redDiff + greenDiff + blueDiff # Total difference
        # Compare difference; find lowest difference
        if totalDiff < lowestDiff:
            lowestDiff = totalDiff
            closestValue = value
    return closestValue

# Check if a colour is grayscale (UI element)
def isGrayScale(colour):
    r, g, b = colour
    avgColour = (r + g + b) / 3 # Obtain pixel's average colour value
    # Check if pixel colours are close to average (GrayScale)
    if abs(r - avgColour) < 10 and abs(g - avgColour) < 10 and abs(b - avgColour) < 10: 
        return True
    return False

# Convert image colours to kWh values based on colour reference
def colourToValue(file):
    pixels = file.load()
    w = file.width
    h = file.height
    values = [] # Store kWh values
    # Iterate through each pixel in image
    for r in range(h):
        for c in range(w):
            colour = pixels[c, r]               # Get pixel colour (tuple)
            if not isGrayScale(colour):         # Ignore grayscale pixels (UI element)
                value = getClosestValue(colour) # Get closest kWh value
                values.append(value)            # Add kWh value to list
    return values

# Calculate consistency of array values (Most common/total values)
def getArrayConsistency(data):
    instances = []                           # Number of instances for each reference value
    for i in range(600, 2500, 100):          # Iterate through reference values
        instances.append(data.count(i))      # Count instances of each reference value
    return max(instances)/sum(instances)*100 # Return consistency percentage (Most common/total values)

# Preform selection sort on nested array based on a reference index
def nestedArraySelectionSort(data, index):
    # Iterate through each element in the array
    for i in range(len(data)):              
        minIndex = i 
        for k in range(i+1, len(data)):                   # Iterate through every element for each element
            if data[k][index] < data[minIndex][index]:    # Compare based on reference index
                minIndex = k
        data[i], data[minIndex] = data[minIndex], data[i] # Swap elements
    return data

# Perform binary search on sorted nested array to find target value with a given tolerance
def nestedArrayBinarySearch(data, target, tolerance, index):
    left = 0               # Left boundary of search range
    right = len(data) - 1  # Right boundary of search range
    closestValue = None    # Store closest match found
    closestDiff = math.inf # Track smallest difference from target 
    
    # Binary search logic
    while left <= right:
        mid = (left + right) // 2     # Calculate middle index
        midValue = data[mid][index]   # Get value at middle index
        diff = abs(midValue - target) # Calculate difference from target
        # Update closest match if current value is closer
        if diff < closestDiff:
            closestDiff = diff
            closestValue = data[mid]
        # Check if within tolerance
        if diff <= tolerance:
            return data[mid]    # Return exact match within tolerance
        elif midValue < target: # Target is in right half
            left = mid + 1      # Move left boundary right
        else:                   # Target is in left half
            right = mid - 1     # Move right boundary left
    return closestValue
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

"""
getClosestValue logic breakdown
1. Extract RGB values from the passed pixel colour (tuple)
2. Initialize lowestDiff variable to infinity to track the smallest colour difference (Set to infinity so any value would be lower)
3. Iterate through each reference kWh value from 600 to 2400 in steps of 100
4. For each reference value, calculate the sum of the absolute differences between the pixel's RGB values and the reference RGB values from colourReference
5. If the calculated total difference is less than the current lowest difference, update the tracked lowest distance to store the current reference value as the closest match
6. After checking all reference values, return the closest kWh value found for the given pixel colour
"""

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

"""
isTargetFeature logic breakdown
1. Extract RGB values from the passed pixel colour (tuple)
2. Calculate the average colour value (grayscale)
3. Check if each RGB value falls within a range of +-10 of the average colour value
4. If all RGB values are close to the average, return True; pixel is a grayscale colour (UI element)
5. If any RGB value deviates significantly from the average, return False; pixel is apart of the desired feature (photovoltaic map)
"""

# Check if a colour is apart of desired data (Not UI element; Apart of photovoltaic map)
def isTargetFeature(colour):
    r, g, b = colour
    avgColour = (r + g + b) / 3 # Obtain pixel's average colour value
    # Check if pixel colours are close to average (GrayScale)
    if abs(r - avgColour) < 10 and abs(g - avgColour) < 10 and abs(b - avgColour) < 10: 
        return False # It is grayscale (UI element), so it is NOT the target feature
    return True # It is NOT grayscale, so it IS the target feature

"""
boxBlur logic breakdown
1. Create a copy of the original image to store the blurred result (prevents reading already-modified pixels)
2. Load pixel data for both the source image and the new target image
3. Iterate through all image pixels
4. For each pixel, check if there are pixels to its left, right, up, down depending on its position
5. Append the pixel's color tuple to an array if it's a target feature (non-grayscale)
6. Calculate the average RGB values of the collected pixels; if none are collected, keep the original pixel
7. Assign the new averaged RGB tuple to the corresponding pixel in the target image
8. Return the processed image
"""

# Apply a box blur to smooth image noise without mixing in grayscale UI pixels
def boxBlur(file):
    blurredFile = file.copy()      # Create copy for output
    pixels = file.load()           # Read from original
    newPixels = blurredFile.load() # Write to copy
    w = file.width
    h = file.height
    # Iterate through all pixels
    for c in range(w):
        for r in range(h):
            colours = []
            # Check current pixel
            currentColor = pixels[c, r]
            if isTargetFeature(currentColor):
                colours.append(currentColor)
            # Check left
            if c > 0:
                leftColor = pixels[c-1, r]
                if isTargetFeature(leftColor):
                    colours.append(leftColor)
            # Check right
            if c < w-1:
                rightColor = pixels[c+1, r]
                if isTargetFeature(rightColor):
                    colours.append(rightColor)
            # Check up
            if r > 0:
                upColor = pixels[c, r-1]
                if isTargetFeature(upColor):
                    colours.append(upColor)
            # Check down
            if r < h-1:
                downColor = pixels[c, r+1]
                if isTargetFeature(downColor):
                    colours.append(downColor)

            # Keep original pixel if target pixels aren't found
            if len(colours) == 0:
                newPixels[c, r] = pixels[c, r]
                continue
            
            # Calculate average RGB values from surrounding colors
            rTotal = 0
            gTotal = 0
            bTotal = 0
            for i in range(len(colours)):
                rTotal += colours[i][0]
                gTotal += colours[i][1]
                bTotal += colours[i][2]
            
            # Set new pixel based only on target pixels
            newPixels[c, r] = (rTotal//len(colours), gTotal//len(colours), bTotal//len(colours))
    return blurredFile

"""
colourToValue logic breakdown
1. Load the pixel data from the provided image file
2. Initialize an empty list to store the kWh values
3. Iterate through each pixel in the image
4. For each pixel, retrieve its colour value
5. Check if the pixel colour is a target feature (not grayscale/UI element) using isTargetFeature function
6. If the pixel is a target feature, use getClosestValue to convert the colour to a kWh value and add it to the list
7. After processing all pixels, return the list of kWh values
"""

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
            if isTargetFeature(colour):       # Check if pixel is target feature (Not grayscale/UI element)
                value = getClosestValue(colour) # Get closest kWh value
                values.append(value)            # Add kWh value to list
    return values

"""
getArrayConsistency logic breakdown
1. Initialize an empty list to store the count of instances for each reference kWh value
2. Iterate through each reference kWh value from 600 to 2400 in steps of 100
3. For each reference value, count how many times it appears in the provided data list and append this count to the instances list
4. Calculate the consistency percentage by dividing the maximum count (most common value) by the total number of values in the data list, then multiplying by 100 (Convert to percentage)
5. Return the calculated consistency percentage
"""

# Calculate consistency of array values (Most common/total values)
def getArrayConsistency(data):
    instances = []                           # Number of instances for each reference value
    for i in range(600, 2500, 100):          # Iterate through reference values
        instances.append(data.count(i))      # Count instances of each reference value
    return max(instances)/sum(instances)*100 # Return consistency percentage (Most common/total values)

"""
nestedArraySelectionSort logic breakdown
1. Iterate through each element in the nested array
2. For each element, start it as the target (min or max) and store its index
3. Compare the current element with every other element in the array based on the specified reference index
4. If a smaller (or larger, depending on order) element is found, update the target index to this new element's index
5. After checking all elements, swap the current element with the target element
6. Continue this process until the entire array is sorted based on the reference index
7. Return the sorted nested array
"""

# Preform selection sort on nested array based on a reference index
def nestedArraySelectionSort(data, index, descending):
    # Iterate through each element in the array
    for i in range(len(data)):              
        targetIndex = i 
        for k in range(i+1, len(data)):                   # Iterate through every element for each element
            if descending:
                if data[k][index] > data[targetIndex][index]: # Compare based on reference index (High to Low)
                    targetIndex = k
            else:
                if data[k][index] < data[targetIndex][index]: # Compare based on reference index (Low to High)
                    targetIndex = k
        data[i], data[targetIndex] = data[targetIndex], data[i] # Swap elements
    return data

"""
nestedArrayBinarySearch logic breakdown
1. Initialize left and right pointers to define the search range within the nested array
2. Set up variables to track the closest value found and the smallest difference from the target
3. While the left pointer is less than or equal to the right pointer, perform the following:
   - Calculate the middle index and retrieve the value at this index based on the specified reference index
   - Calculate the absolute difference between this middle value and the target value
   - If this difference is smaller than the smallest difference tracked, update the closest value and smallest difference
   - Check if the difference is within the specified tolerance; if so, return the middle element as an exact match
   - If the middle value is less than the target, move the left pointer to the right of the middle index
   - If the middle value is greater than the target, move the right pointer to the left of the middle index
4. If the loop ends without finding an exact match within tolerance, return the closest value found
"""

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
    
    # If closest match is within tolerance, return it; otherwise return None
    if closestDiff <= tolerance:
        return closestValue
    return None
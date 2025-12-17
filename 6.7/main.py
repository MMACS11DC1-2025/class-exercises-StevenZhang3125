from PIL import Image
import utils
import time

# Get user input for kW of solar panels
kW = input("How many kilo-Watts of solar panels are applicable? (Ex. House - 5kW; Warehouse - 100kW; Solar Farm - 50000kW)\n").strip(" .!?")

# Invalid input error handling
try:
    kW = float(kW) # Convert input to float; prepare for math operations
except:
    print("Invalid input; using default (1kW).")
    kW = 1 # Default to 1kW if input is invalid

imageData = [] # Store image data (image number, average kWh, consistency)

globalStartTime = time.time() # Start global timer
# Process each image
for image in range(1, 11):
    # Attempt to open image file (permits missing files)
    try:
        file = Image.open(f"6.7/images/image_{image}.png") # Open image file
        file = file.convert("RGB")                         # Convert image to RGB format (Prevent RGBA/opacity issues)
    except:
        continue
    startTime = time.time()                                   # Start timer for individual image processing
    imageValue = utils.colourToValue(file)                    # Convert image colours to kWh values
    avgkWh = (sum(imageValue) / len(imageValue))*kW           # Calculate average kWh based on kW input and image value
    colourConsistency = utils.getArrayConsistency(imageValue) # Calculate colour/value consistency
    imageData.append((image, avgkWh, colourConsistency))      # Store image data
    endTime = time.time()                                     # End timer for individual image processing

    # Display image results
    print(f"\nLocation {image}; Image {image}")
    print("-----------------------------------------------------------------")
    print(f"You'll average {(avgkWh):.2f} kWh for the region in image {image}.") # Display average kWh
    print(f"The consistency of the region's kWh is {colourConsistency:.2f}%")    # Display consistency
    print(f"Image {image} processing took {endTime - startTime:.3f}s")           # Display processing time

globalEndTime = time.time()                                                              # End global timer
print(f"\nTotal processing time for all images: {globalEndTime - globalStartTime:.3f}s") # Display total processing time (all images)

# Loop to allow several input attempts/variations
while True:
    # Display ranking options
    print("\n1) Rank average kWh images")
    print("2) Rank kWh consistency")
    print("3) Find specific average kWh value")
    print("4) Find specific consistency value")
    print("5) Exit")
    option = input("Selection: ").strip(" .!?")
    # Invalid input error handling
    try:
        option = int(option)
    except:
        print("Please enter a number corresponding to the options.")
        continue    
    
    # Present order options (for ranking options 1 and 2)
    if option == 1 or option == 2:
        print("1) Low to High")
        print("2) High to Low")
        order = input("Selection: ").strip(" .!?")
        # Invalid input error handling
        try:
            order = int(order)
        except:
            print("Please enter a number corresponding to the options.")
            continue

    # Process ranking based on average kWh
    if option == 1:
        sortedArray = utils.nestedArraySelectionSort(imageData, 1) # Sort based on average kWh
        orderText = "Lowest to Highest"                     # Default order text
        if order == 2:                                      # Check user order preference
            sortedArray = sortedArray[::-1]                               # Reverse order of data (Low to High -> High to Low)
            orderText = "Highest to Lowest"                 # Update order text
        sortedArray = sortedArray[0:5]                                    # Splice top 5 results from data

        # Display ranking results
        print(f"\nTop 5 Average kWh Rankings: ({orderText})")
        # Iterate through each of the top 5 results
        for image in range(len(sortedArray)):
            imgNumber = sortedArray[image][0]         # Image number
            avgkWh = sortedArray[image][1]            # Average kWh
            colourConsistency = sortedArray[image][2] # Colour consistency
            # Display ranking results
            print(f"\nAverage kWh Ranking {image+1}; Location {imgNumber}; Image {imgNumber}")
            print("-----------------------------------------------------------------")
            print(f"You'll average {(avgkWh):.2f} kWh for the region in image {imgNumber}.")
            print(f"The consistency of the region's kWh is {colourConsistency:.2f}%")

    # Process ranking based on kWh consistency
    elif option == 2:
        sortedArray = utils.nestedArraySelectionSort(imageData, 2) # Sort based on kWh consistency
        orderText = "Lowest to Highest"                     # Default order text 
        if order == 2:                                      # Check user order preference
            sortedArray = sortedArray[::-1]                               # Reverse order of data (Low to High -> High to Low)
            orderText = "Highest to Lowest"                 # Update order text
        sortedArray = sortedArray[0:5]                                    # Splice top 5 results from data

        # Display ranking results
        print(f"\nTop 5 Consistency Rankings: ({orderText})")
        # Iterate through each of the top 5 results
        for image in range(len(sortedArray)):
            imgNumber = sortedArray[image][0]         # Image number
            avgkWh = sortedArray[image][1]            # Average kWh
            colourConsistency = sortedArray[image][2] # Colour consistency
            # Display ranking results
            print(f"\nConsistency Ranking {image+1}; Location {imgNumber}; Image {imgNumber}")
            print("-----------------------------------------------------------------")
            print(f"You'll average {(avgkWh):.2f} kWh for the region in image {imgNumber}.")
            print(f"The consistency of the region's kWh is {colourConsistency:.2f}%")

    # Search for specific average kWh value
    elif option == 3:
        # Get target kWh value from user
        targetkWh = input("Enter target average kWh value: ").strip(" .!?")
        # Invalid input error handling
        try:
            targetkWh = float(targetkWh) # Convert input to float; prepare for math operations
        except:
            print("Invalid input; please enter a number.")
            continue

        # Get tolerance from user
        tolerance = input("Enter tolerance: ").strip(" .!?")
        # Invalid input error handling
        try:
            tolerance = float(tolerance) # Convert input to float; prepare for math operations
        except:
            print("Invalid input; please enter a number.")
            continue
        
        sortedArray = utils.nestedArraySelectionSort(imageData, 1)                   # Sort based on average kWh
        result = utils.nestedArrayBinarySearch(sortedArray, targetkWh, tolerance, 1) # Binary search for target kWh
        
        # If a result was found, display it
        if result:
            imgNumber = result[0]                # Image number
            avgkWh = result[1]                   # Average kWh
            colourConsistency = result[2]        # Colour consistency
            difference = abs(avgkWh - targetkWh) # Calculate difference from target
            
            # Display search results
            print(f"\nSearch Result for Target kWh: {targetkWh:.2f} ({tolerance:.2f} tolerance)")
            print(f"Location {imgNumber}; Image {imgNumber}")
            print("-----------------------------------------------------------------")
            print(f"Average kWh: {avgkWh:.2f} kWh")
            print(f"Consistency: {colourConsistency:.2f}%")
            print(f"Difference from target: {difference:.2f} kWh")
        else:
            print("\nNo matching location found.")
    
    # Search for specific consistency value
    elif option == 4:
        # Get target consistency from user
        targetConsistency = input("Enter target consistency percentage: ").strip(" .!?")
        # Invalid input error handling
        try:
            targetConsistency = float(targetConsistency) # Convert input to float; prepare for math operations
        except:
            print("Invalid input; please enter a number.")
            continue

        # Get tolerance from user
        tolerance = input("Enter tolerance: ").strip(" .!?")
        # Invalid input error handling
        try:
            tolerance = float(tolerance) # Convert input to float; prepare for math operations
        except:
            print("Invalid input; please enter a number.")
            continue
        
        sortedArray = utils.nestedArraySelectionSort(imageData, 2)                           # Sort based on consistency
        result = utils.nestedArrayBinarySearch(sortedArray, targetConsistency, tolerance, 2) # Binary search for target consistency
        
        # If a result was found, display it
        if result:
            imgNumber = result[0]                                   # Image number
            avgkWh = result[1]                                      # Average kWh
            colourConsistency = result[2]                           # Colour consistency
            difference = abs(colourConsistency - targetConsistency) # Calculate difference from target
            
            # Display search results
            print(f"\nSearch Result for Target Consistency: {targetConsistency:.2f}% ({tolerance:.2f} tolerance)")
            print(f"Location {imgNumber}; Image {imgNumber}")
            print("-----------------------------------------------------------------")
            print(f"Average kWh: {avgkWh:.2f} kWh")
            print(f"Consistency: {colourConsistency:.2f}%")
            print(f"Difference from target: {difference:.2f}%")
        else:
            print("\nNo matching location found.")

    # Exit program/loop
    if option == 5:
        break
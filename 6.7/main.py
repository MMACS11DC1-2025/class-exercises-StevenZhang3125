from PIL import Image
import utils
import time

kW = input("How many kilo-Watts of solar panels are applicable? (Ex. House - 5kW; Warehouse - 100kW; Solar Farm - 50000kW)\n").strip(" .!?")
try:
    kW = float(kW)
except:
    print("Invalid input; using deafault (1kW).")
    kW = 1
imageData = []

globalStart = time.time()
for i in range(1, 11):
    try:
        file = Image.open(f"6.7/images/image_{i}.png")
        file = file.convert("RGB")
    except:
        continue
    start = time.time()
    values = utils.colourToValue(file)
    avg = (sum(values) / len(values))*kW
    consistency = utils.datasetConsistency(values)
    imageData.append((i, avg, consistency))
    end = time.time()

    print(f"\nLocation {i}; Image {i}")
    print("-----------------------------------------------------------------")
    print(f"You'll average {(avg):.2f} kWh for the region in image {i}.")
    print(f"The consistency of the region's kWh is {consistency:.2f}%")
    print(f"Image {i} processing took {end - start:.2f}s")

globalEnd = time.time()
print(f"\nTotal processing time for all images: {globalEnd - globalStart:.2f}s")

while True:
    print("\n1) Rank average kWh images")
    print("2) Rank kWh consistency")
    print("3) Exit")
    option = input("Selection: ").strip(" .!?")
    try:
        option = int(option)
    except:
        print("Please enter a number corresponding to the options.")
        continue    
    print("1) Low to High")
    print("2) High to Low")
    order = input("Selection: ").strip(" .!?")
    try:
        order = int(order)
    except:
        print("Please enter a number corresponding to the options.")
        continue
    if option == 1:
        data = utils.nestedDatasetSelectionSort(imageData, 1)
        orderMode = "Lowest to Highest"
        if order == 2:
            data = data[::-1]
            orderMode = "Highest to Lowest"
        data = data[0:5]
        print(f"\nTop 5 Average kWh Rankings: ({orderMode})")
        for i in range(len(data)):
            img = data[i][0]
            avg = data[i][1]
            consistency = data[i][2]
            print(f"\nAverage kWh Ranking {i+1}; Location {img}; Image {img}")
            print("-----------------------------------------------------------------")
            print(f"You'll average {(avg):.2f} kWh for the region in image {i}.")
            print(f"The consistency of the region's kWh is {consistency:.2f}%")
    elif option == 2:
        data = utils.nestedDatasetSelectionSort(imageData, 2)
        orderMode = "Lowest to Highest"
        if order == 2:
            data = data[::-1]
            orderMode = "Highest to Lowest"
        data = data[0:5]
        print(f"\nTop 5 Consistency Rankings: ({orderMode})")
        for i in range(len(data)):
            img = data[i][0]
            avg = data[i][1]
            consistency = data[i][2]
            print(f"\nConsistency Ranking {i+1}; Location {img}; Image {img}")
            print("-----------------------------------------------------------------")
            print(f"You'll average {(avg):.2f} kWh for the region in image {i}.")
            print(f"The consistency of the region's kWh is {consistency:.2f}%")
    elif option == 3:
        break
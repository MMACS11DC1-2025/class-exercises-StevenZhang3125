from PIL import Image
import utils

kW = int(input("How many kilo-Watts of solar panels are applicable? (Ex. House - 5kW; Warehouse - 100kW; Solar Farm - 50000kW\n"))
imageData = []

for i in range(1, 4):
    try:
        file = Image.open(f"6.7/images/image_{i}.png")
        file = file.convert("RGB")
    except:
        continue
    
    values = utils.colourToValue(file)
    avg = (sum(values) / len(values))*kW
    consistency = utils.datasetConsistency(values)
    imageData.append((i, avg, consistency))

    print(f"\nLocation {i}; Image {i}")
    print("-----------------------------------------------------------------")
    print(f"You'll average {(avg):.2f} kWh for the region in image {i}.")
    print(f"The consistency of the region's kWh is {consistency:.2f}%")

option = True
while option:
    print("\n1) Show lowest to highest average kWh images")
    print("2) Show lowest to highest kWh consistency")
    option = int(input("Selection (Enter to quit): "))
    if option == 1:
        data = utils.nestedDatasetSelectionSort(imageData, 1)
        for i in range(len(data)):
            img = data[i][0]
            avg = data[i][1]
            consistency = data[i][2]
            print(f"\nLocation {img}; Image {img}")
            print("-----------------------------------------------------------------")
            print(f"You'll average {(avg):.2f} kWh for the region in image {i}.")
            print(f"The consistency of the region's kWh is {consistency:.2f}%")
    elif option == 2:
        data = utils.nestedDatasetSelectionSort(imageData, 2)
        for i in range(len(data)):
            img = data[i][0]
            avg = data[i][1]
            consistency = data[i][2]
            print(f"\nLocation {img}; Image {img}")
            print("-----------------------------------------------------------------")
            print(f"You'll average {(avg):.2f} kWh for the region in image {i}.")
            print(f"The consistency of the region's kWh is {consistency:.2f}%")
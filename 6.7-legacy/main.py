from PIL import Image
import utils

for i in range(0, 10):
    try:
        file = Image.open(f"6.7/images/image_{i+1}.png")
        file = file.convert("RGB")
    except:
        continue
    gray = utils.colourInterest(file)
    whiteLines = utils.whiteLinesFinder(file, (0, 0))
    
    pixels = file.load()
    w = file.width
    h = file.height
    for j in range(len(whiteLines)):
        for k in range(len(whiteLines[j])):
            x, y = whiteLines[j][k]
            pixels[x, y] = (255, 0, 0)
    
    # for m in range(len(blacklist)):
    #     for n in range(len(blacklist[m])):
    #         x, y = blacklist[m][n][0], blacklist[m][n][1]
    #         pixels[x, y] = (0, 255, 0)
    file.save(f"6.7/images/result_image_{i+1}.png")
    print(f"Image {i+1} processed.")


from PIL import Image
import utils

for i in range(10):
    try:
        file = Image.open(f"6.7/images/image_{i+1}.png")
        file = file.convert("RGB")
    except:
        continue
    gray = utils.colourInterest(file)
    blacklist = utils.otherColours(file, gray)
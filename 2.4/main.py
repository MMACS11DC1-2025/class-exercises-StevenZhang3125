file = open("2.4/responses.csv")
for line in file:
    line = line.split(",")
    if line[1].lower() == "steven zhang":
        print(line)
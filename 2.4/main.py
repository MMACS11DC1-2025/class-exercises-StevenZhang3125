file = open("2.4/responses.csv")
for line in file:
    line = line.split(",")
    if line[1] == "Steven Zhang":
        print(line)
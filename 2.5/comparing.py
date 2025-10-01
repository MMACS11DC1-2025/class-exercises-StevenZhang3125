"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

"""
Idea:
Least similar finder
Requests the user to input a name and outputs the least similar person

Algorithm:
1) Declare variables (Lowest similarities) 
2) Skip the first line in the file and iterate through the rest of the data.
3) Iterates through the file to find the inputed user and saves it a variable.
4) Iterate through each element of each line to compare elements that could be compared (Favourite ____ and not Name or ID)
5) Compare which element are equal and count to a temporary variable
6) Compare the lowest similarity value to the temporary variable 
7) If the temporary value is lower, change the lowest similarity value
8) Display who is the least similar to the inputed person and by how few
"""

file = list(open("2.4/responses.csv"))
junk = file.pop(0)

lowest = 999

print("Least Similar Person Finder")
print("Enter an person and it will find who is least similar to that person!")
person = input("Name: ").lower().strip(".!? ")

# Find the inputed person and format list
for i in range(len(file)):
    file[i] = file[i].split(",")
    if file[i][1].lower().strip(" .?!") == person:
        personLine = file[i]

# For each person
for i in range(len(file)):
    # For each element
    for k in range(len(file[i])):
        


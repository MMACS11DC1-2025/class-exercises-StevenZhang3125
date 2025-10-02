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
Similarity Leaderboard
Requests the user to input a name and outputs a leaderboard of similarity values

Algorithm:
1) Declare variables, convert file to List (More easily indexable)
2) Skip the first line in the file and iterate through the rest of the data.
3) Iterates through the file to find the inputed user and saves it a variable.
4) Iterate through each element of each line to compare elements that could be compared (Favourite ____ and not Name or ID)
5) Compare which element are equal and count to a temporary variable
6) Add compared data to leaderboard
7) Display who is the least similar to the inputed person and by how few

Test Cases:
Steven Zhang
1

Steven Zhang
2

Steven zhAng!!?  
1

Even Chen
1
"""

# Opens csv File and converts to list (more easily indexable)
file = list(open("2.4/responses.csv"))
# Removes first line/element (Legend)
junk = file.pop(0)

while True:
    # User Instructions
    print("Similarity Leaderboard")
    print("Enter an person and find out who is most to least (or vise versa) similar to that person!")

    # User Input Requests
    person = input("Name: ").lower().strip(".!? ")
    order = int(input("1) Most to Least\n2) Least to Most\nEnter which one (1/2): "))

    # Converts integer input (order) into boolean
    if order == 1:
        order = True
    else:
        order = False

    # Delcares empty leaderboard variable
    leaderboard = []

    # Find the inputed person and formats list (.split(","); Completing conversion from csv file to List)
    # Declare empty list for inputed person; useful to determine if the person has been found
    personLine = []
    # Iterate through each line of the list and properly convert data to nested lists 
    for i in range(len(file)):
        file[i] = file[i].split(",")
        # Checks if line belongs to entered person
        if file[i][1].lower().strip(" .?!") == person:
            # Sets empty list to entered person's data; shows person has been found
            personLine = file[i]

    # Checks person's list for changes, if no changes were made, the person was not found
    if personLine == []:
        print("\nSorry, could not find that person. Please check your spelling and try again.")
        continue

    # Iterates through the list of people's data
    for i in range(len(file)):
        # Declares a variable, set to 0 for each person
        similarities = 0
        # Iterates through each element of the person 
        for k in range(len(file[i])):
            # Skips ID and Name elements
            if k == 0 or k == 1:
                continue
            # Skips self (entered user)
            if file[i][1].lower().strip(" .?!") == person:
                continue
            # If elements are the same, increase similarities by 1
            if file[i][k].lower().strip(" .!?") == personLine[k].lower().strip(" .?!"):
                similarities += 1
        
        # Adds person's name and similaries to the entered person into the leader board (unsorted)
        leaderboard.append([file[i][1], similarities])

    # Source for sorting nested list -> https://stackoverflow.com/questions/65679123/sort-nested-list-data-in-python
    # Sorts the nested list leaderboard according to the variable order, fullfilling the users request for how the data should be ordered
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=order)

    # Formats display text according to sorted order
    if order:
        print("Increasing Order")
    else:
        print("Decreasing Order")

    # Header for the leaderboard
    print("Rank | Person | Similarities | Increasing")
    
    # Iterates through the leaderboard and displays every element in request order
    for i in range(len(leaderboard)):
        print(str(i+1) + ") " + leaderboard[i][0] + " " + str(leaderboard[i][1]))
    
    # Exits out of while loop
    break

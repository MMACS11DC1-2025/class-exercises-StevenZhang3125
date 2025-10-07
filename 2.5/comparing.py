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
Similarity Leaderboard and Finder
Requests the user to input a name and choose whether to output a leaderboard of similarity 
values or who is most/least similar to that person

Algorithm (Most/Least Similar Person):
1) Declare variables, convert file to List (More easily indexable)
2) Skip the first line in the file and iterate through the rest of the data
3) Request a name and options
4) Iterates through the file to find the inputed user and saves it a variable
5) Iterate through each element of each line to compare elements that could be compared (Favourite ____ and not Name or ID)
6) Compare which element are equal and count to a temporary variable
7) Compare the temporary variable to the saved variable of the inputed person
8) Display who is the most/least similar to the inputed person and by how much

Algorithm (Leaderboard):
1) Declare variables, convert file to List (More easily indexable)
2) Skip the first line in the file and iterate through the rest of the data
3) Request a name and options
4) Iterates through the file to find the inputed user and saves it a variable
5) Iterate through each element of each line to compare elements that could be compared (Favourite ____ and not Name or ID)
6) Compare which element are equal and count to a temporary variable
7) Add compared data to leaderboard
8) Display who is the least similar to the inputed person and by how few

Test Cases:

    Input:
    Steven Zhang
    1

    Expected Output:
    Person: Jayden Wong | Similarity Count: 4

    Input:
    Steven Zhang
    2

    Expected Output:
    Person: Ashar Siddiqui | Similarity Count: 0

    Input:
    Steven Zhang
    3
    1

    Expected Output:
    1) Jayden Wong 4 
    ...
    26) Erisha Rahman 0

    Input:
    Steven Zhang
    3
    2

    Expected Output:
    1) Ashar Siddiqui 0
    ...
    26) Daichi Lee 4


    Input:
    SteVen ZhAng!!!
    1

    Expected Output:
    Person: Jayden Wong | Similarity Count: 4

    Input:
    Even Chen
    1

    Expected Output:
    Sorry, could not find that person. Please check your spelling and try again.
    
"""

# Opens csv File and converts to list (more easily indexable)
file = list(open("2.4/responses.csv"))
# Removes first line/element (Legend)
junk = file.pop(0)

# Function for displaying most or least similar person
def mostLeastFinder(comparePerson, compareLine, config):
    # Declare vertex similarity depending on user configuration
    if config:
        vertexSimilarity = 0
    else:
        vertexSimilarity = 999
    similarityPerson = ""

    # Iterates through the list of people's data
    for i in range(len(file)):
        # Skips self (entered user)
        if file[i][1].lower().strip(" .?!") == comparePerson:
            continue
        # Declares a variable, set to 0 for each person
        similarities = 0
        # Iterates through each element of the person 
        for k in range(len(file[i])):
            # Skips ID and Name elements
            if k == 0 or k == 1:
                continue
            # If elements are the same, increase similarities by 1
            if file[i][k].lower().strip(" .!?") == compareLine[k].lower().strip(" .?!"):
                similarities += 1
        # Compare similarity value with vertex similarity (max/min) and changes variables when conditions are met
        if config:
            if similarities > vertexSimilarity:
                vertexSimilarity = similarities
                similarityPerson = file[i][1]
        else:
            if similarities < vertexSimilarity:
                vertexSimilarity = similarities
                similarityPerson = file[i][1]

    # Formats display text according to user configuration
    if config:
        print("Most similiar")
    else:
        print("Least similiar")
    
    # Display information
    print("Person: " + similarityPerson + " | Similarity Count: " + str(vertexSimilarity))

# Function for displaying similarity leaderboard in order according to user
def leaderboardFinder(comparePerson, compareLine, sortOrder):
    # Delcares empty leaderboard variable
    leaderboard = []

    # Iterates through the list of people's data
    for i in range(len(file)):
        # Skips self (entered user)
        if file[i][1].lower().strip(" .?!") == comparePerson:
            continue
        # Declares a variable, set to 0 for each person
        similarities = 0
        # Iterates through each element of the person 
        for k in range(len(file[i])):
            # Skips ID and Name elements
            if k == 0 or k == 1:
                continue
            # If elements are the same, increase similarities by 1
            if file[i][k].lower().strip(" .!?") == compareLine[k].lower().strip(" .?!"):
                similarities += 1
        
        # Adds person's name and similaries to the entered person into the leader board (unsorted)
        leaderboard.append([file[i][1], similarities])

    # Source for sorting nested list -> https://stackoverflow.com/questions/65679123/sort-nested-list-data-in-python
    # Sorts the nested list leaderboard according to the variable order, fullfilling the users request for how the data should be ordered
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=sortOrder)

    # Formats display text according to sorted order
    if sortOrder:
        print("Increasing Order")
    else:
        print("Decreasing Order")

    # Header for the leaderboard
    print("Rank | Person | Similarities | Increasing")
    
    # Iterates through the leaderboard and displays every element in request order
    for i in range(len(leaderboard)):
        print(str(i+1) + ") " + leaderboard[i][0] + " " + str(leaderboard[i][1]))

# Prevent errors on double formatting
formatted = False
while True:
    # User Instructions
    print("Similarity Leaderboard and Finder")
    print("----------------------------------")
    print("Enter an person and find out who are the most or least similar to that person!")
    print("They may be several people that have share the first or last place; only one will be displayed.")
    print("If you would like to see everyone, choose the leaderboard option instead.")

    # User Input Requests
    person = input("Name: ").strip(".!? ").lower()
    # User misinput safeguard
    while True:
        option = int(input("1) Most Similar\n2) Least Similar\n3) Leaderboard\nPlease enter a number (1/2/3): ").strip(" .?!"))
        # Break out of loop if input is valid
        if option >= 1 and option <= 3:
            break
        print("\nPlease enter a valid selection (1/2/3)\n")
    if option == 3:
        # User misinput safeguard
        while True:
            order = int(input("1) Most to Least\n2) Least to Most\nEnter which one (1/2): "))
            # Break out of loop if input is valid
            if order == 1 or order == 2:
                break
            print("\nPlease enter a valid selection (1/2)\n")

    # Declare empty list for inputed person; will be used to determine if the person has been found
    personLine = []

    # Iterate through each line of the list and properly convert data to nested lists 
    for i in range(len(file)):
        # Prevent errors on double formatting; checks if list is already properly formatted
        if not formatted:
            file[i] = file[i].split(",")
        # Checks if line belongs to entered person
        if file[i][1].lower().strip(" .?!") == person:
            # Sets empty list to entered person's data; shows person has been found
            personLine = file[i]
    formatted = True

    # Checks person's list for changes, if no changes were made, the person was not found
    if personLine == []:
        print("\nSorry, could not find that person. Please check your spelling and try again.\n")
        continue

    # Calls correct function with set configuration based on user inputs
    if option == 1:
        mostLeastFinder(person, personLine, True)
    elif option == 2:
        mostLeastFinder(person, personLine, False)
    else:
        if order == 1:
            leaderboardFinder(person, personLine, True)
        else:
            leaderboardFinder(person, personLine, False)
    break


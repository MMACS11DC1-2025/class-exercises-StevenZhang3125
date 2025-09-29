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
1) Declare variables (Similarities)
2) Iterates through the file to find the inputed user and saves it a variable.
3) Skip the first line in the file and iterate through the rest of the data.
4) Iterate through each element of each line to compare elements that could be compared (Favourite ____ and not Name or ID)
5) Compare which element are equal and add to a temporary element
"""
file = open("2.4/responses.csv")


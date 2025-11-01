import turtle
import random

# Recursive spiral squares drawing function
def drawSquare(turtle, size, colour, colourIndex, fill, target, current):
    # Base case/Terminating case
    if target == current:
        return 0
    
    # Return to first colour in range if index is at the end (loop)
    if colourIndex == len(colours[colour]):
        colourIndex = 0

    # Set filling colour and begin filling if fill mode is enabled
    if fill:
        turtle.fillcolor(colours[colour][colourIndex])
        turtle.begin_fill()

    # Set turtle's colour
    turtle.color(colours[colour][colourIndex])

    # Set turtle's speed and stoke (both constant)
    turtle.speed(0)
    turtle.pensize(2)

    # Draw square
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

    # End filling if fill mode is enabled
    if fill:
        turtle.end_fill()
    
    # Rotate turtle 5 degrees left to create spiralling staricase effect 
    turtle.left(5)

    # Calls itself for the next square and returns itself + 1 for counting the total squares drawn
    return drawSquare(turtle, size*0.99, colour, colourIndex+1, fill, target, current+1) + 1

# Dictionary of colour ranges
colours = {
    "reds": ["#FF0000", "#FF4D4D", "#FF6666", "#CC0000", "#B22222"],
    "greens": ["#00FF00", "#32CD32", "#66FF66", "#228B22", "#008000"],
    "blues": ["#0000FF", "#1E90FF", "#3399FF", "#4682B4", "#4169E1"],
    "rainbow": ["red", "orange", "yellow", "green", "blue", "purple"]
}

# Dictionary of dynamic comments for guesses taken
comments = {
    "good": ["Nice!", "Well done!", "Wow, nice job!"],
    "medicore": ["Not bad.", "Could be better.", "Not terrible."],
    "poor": ["Tragic.", "Not great.", "Unfortunate."]
}

# Declare turtle variable
pointer = turtle.Turtle()

# User draw mode selection
# While loop used to allow user reinputs if inital input is invalid
while True:
    print("\nPlease select a draw mode")
    print("-------------------------")
    mode = input("Solid\nOutline\nSelect a mode: ").lower().strip(" .!?")

    # Translates mode selection into fill condition
    if mode == "solid":
        fill = True
    elif mode == "outline":
        fill = False

    # Invalid user input handler
    else:
        print("Please type either \"Solid\" or \"Outline\"")
        continue
    break

# User colour range selection
# While loop used to allow user reinputs if inital input is invalid
while True:
    print("\nPlease select a colour range")
    print("------------------------------")
    colour = input("Reds\nGreens\nBlues\nRainbow\nSelect a colour range: ").lower().strip(" .!?")

    # Invalid user input handler
    if colour not in colours:
        print("Please type either \"Reds\", \"Greens\", \"Blues\", or \"Rainbow\"")
        continue
    break

# Initialize guess as false; used as a condition to determine which mode was selected
guess = False

# User square count method selection
# While loop used to allow user reinputs if inital input is invalid
while True:
    print("\nHow many square would you like to be drawn?")
    print("---------------------------------------------")
    mode = int(input("\n1) Random\n2) Random and Guess how many\n3) Custom\nSelect a mode: "))

    # Translates mode selection into respective configureation
    if mode == 1:
        count = random.randint(10, 100)
    elif  mode == 2:
        guess = True
        guessCount = -1     # Set to -1 becuase while loop adds 1 on first run before the user has guessed
        count = random.randint(10, 100)
    elif mode == 3:
        count = int(input("Enter the number of sqaures you would like to be drawn: "))

    # Invalid user input handler
    else:
        print("Please type either 1, 2, or 3")
        continue
    break

# Run recurive function with user determined configuration
squares = drawSquare(pointer, 200, colour, 0, fill, count, 0)

# Runs if square count method is set to 2/Random and Guess how many 
if guess:
    print("Without counting, how many squares do you think there are?")
    while guess != squares:
        guessCount += 1
        guess = int(input())

        # Hints for the user relative to their guess
        if guess > squares:
            print("Guess lower, try again.")
        if guess < squares:
            print("Guess higher, try again.")
    # Displays correct answer and how many guesses it took
    print("Correct! There are " + str(squares) + " squared drawn.")
    print("It took you " + str(guessCount) + " amount of tries.")

    # Displays a dynamic random comment based on preformance of guesses took
    if guessCount <= 3:
        print(random.choice(comments["good"]))
    elif guessCount <= 6:
        print(random.choice(comments["medicore"]))
    else:
        print(random.choice(comments["poor"]))
# Runs if square count method is set to 1 or 3/Random or Custom
else:
    # Special number conditional
    if squares == 67:
        print(str(squares) + " squares were drawn... 👀")
    # Mundane number statement
    else:
        print(str(squares) + " squares were drawn.")

# Finish program
turtle.done()
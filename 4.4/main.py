import turtle

def drawSquare(turtle, size, speed, colour, mode, target, current):
    fill = mode == 3 or mode == 4
    if target == current:
        return
    if colour == len(colours):
        colour = 0
    if fill:
        turtle.fillcolor(colours[colour])
    turtle.color(colours[colour])
    turtle.speed(speed)
    if fill:
        turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    if fill:
        turtle.end_fill()
    turtle.left(5)
    if mode == 2 or mode == 4:
        drawSquare(turtle, size*0.99, speed, colour+1, mode, target, current+1)
    else:
        drawSquare(turtle, size*0.99, speed, colour, mode, target, current+1)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
pointer = turtle.Turtle()
colour = 0
mode = int(input("1) Solid Outline\n2) Rainbow Outline\n3) Solid Fill\n4) Sold Raindbow\nEnter a number selection: "))
if mode == 1 or mode == 3:
    colour = int(input("1) Red\n2) Orange\n3) Yellow\n4) Green\n5) Blue\n6) Purple\nEnter a number selecion: "))
    colour -= 1
count = int(input("Enter the number of sqaures you would like to be drawn: "))
drawSquare(pointer, 200, 0, colour, mode, count, 0)

turtle.done()
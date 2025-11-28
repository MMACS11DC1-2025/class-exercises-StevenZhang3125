import turtle

# create a turtle
wave = turtle.Turtle()
wave.shape("arrow")     # looks like a little turtle
wave.color("black")
wave.pensize(3)

def zigZag(dips, speed):
    wave.speed(speed)
    wave.penup()
    wave.goto(-250, 50)
    wave.pendown()
    y = 50
    x = -250
    for i in range(dips+1):
        y = -y
        x += 500/(dips+1)
        wave.goto(x, y)
        
while True:
    dips = int(input("How many zigs in the zag? : "))
    speed = int(input("How fast should it go? : "))
    zigZag(dips, speed)
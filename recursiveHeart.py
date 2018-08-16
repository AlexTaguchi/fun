# Draw a Recursive Heart with Turtle Module
import turtle


# Recursive function
def heart(turt, stride):

    # Base case
    if stride < 1:
        return

    # Heart drawing parameters
    adjust = 1.25
    turt.width(stride)

    # Draw the heart
    for _ in range(50):
        turt.forward(stride)
        turt.right(5)
    for _ in range(20):
        turt.forward(adjust*stride)
        turt.left(3)
    turt.forward(adjust*stride)
    turt.right(160)
    for _ in range(20):
        turt.forward(adjust*stride)
        turt.left(3)
    for _ in range(50):
        turt.forward(stride)
        turt.right(5)
    turt.forward(stride)
    turt.left(180)

    # Recursively draw smaller hearts until base case reached
    heart(turt, stride-1)


# Instantiate turtle object
t = turtle.Turtle()
t.color('red')
t.speed(100)
t.hideturtle()
t.up()

# Put turtle into correct initial position
t.left(90)
t.forward(100)
t.down()

# Draw five hearts
heart(t, 5)

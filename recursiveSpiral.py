# Draw a Recursive Spiral with Turtle Module
import turtle


# Recursive function
def spiral(turt, stride):

    # Base case
    if stride < 0:
        return

    # Recursive calls
    turt.width(500/stride)
    turt.forward(stride)
    turt.right(35)
    spiral(turt, stride-1)


# Instantiate turtle object
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.up()

# Position turtle
t.left(110)
t.forward(300)
t.right(110)
t.down()

# Draw spirals
spiral(t, 200)

# Draw a Fractal Tree with Turtle Module
import turtle


# Recursive function
def tree(turt, stride):

    # Base case
    if stride < 1:
        return

    # Tree drawing parameter
    angle = 20

    # Recursive calls
    turt.width(stride/10)
    turt.forward(stride)
    turt.right(angle)
    tree(turt, stride-10)
    turt.left(2*angle)
    tree(turt, stride-10)
    turt.right(angle)
    turt.back(stride)


# Instantiate turtle object
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.up()

# Position turtle
t.left(90)
t.back(200)
t.down()

# Draw tree
tree(t, 80)

# Draw Fractal Snowflake with Turtle Module
import turtle


# Recursive function
def snowflake(turt, stride):

    # Base case
    if stride < 1.5:
        return

    # Draw one side of the snowflake recursively
    turt.forward(stride)
    snowflake(turt, stride/2)
    turt.forward(stride)
    turt.left(60)
    turt.forward(stride)
    snowflake(turt, stride/2)
    turt.forward(stride)
    turt.right(120)
    turt.forward(stride)
    snowflake(turt, stride / 2)
    turt.forward(stride)
    turt.left(60)
    turt.forward(stride)
    snowflake(turt, stride / 2)
    turt.forward(stride)


# Instantiate turtle object
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.up()

# Put turtle into correct initial position
t.left(120)
t.forward(300)
t.right(120)
t.down()

# Draw three snowflakes
for (i, j) in enumerate([10, 8, 6]):

    # Snowflake fractal
    t.width(i + 1)
    for _ in range(3):
        snowflake(t, j)
        t.right(120)

    # Reposition
    t.right(30)
    t.up()
    t.forward(32)
    t.down()
    t.left(30)

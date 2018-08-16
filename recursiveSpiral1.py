# Draw a recursive spiral

import turtle


def spiral(turt, stride):
    if stride < 0:
        return
    turt.width(500/stride)
    turt.forward(stride)
    turt.right(35)
    spiral(turt, stride-1)


t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.up()
t.left(110)
t.forward(300)
t.right(110)
t.down()
spiral(t, 200)
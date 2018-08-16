# Draw a recursive heart

import turtle


def heart(turt, stride):
    if stride < 1:
        return
    adjust = 1.25
    turt.width(stride)
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
    heart(turt, stride-1)


t = turtle.Turtle()
t.color('red')
t.speed(100)
t.hideturtle()
t.up()
t.left(90)
t.forward(100)
t.down()
heart(t, 5)
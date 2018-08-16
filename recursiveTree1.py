# Draw a fractal tree

import turtle


def tree(turt, stride):
    if stride < 1:
        return
    turt.width(stride/10)
    turt.forward(stride)
    angle = 20
    turt.right(angle)
    tree(turt, stride-10)
    turt.left(2*angle)
    tree(turt, stride-10)
    turt.right(angle)
    turt.back(stride)


t = turtle.Turtle()
t.hideturtle()
t.up()
t.left(90)
t.back(200)
t.down()
t.speed(100)
tree(t, 80)
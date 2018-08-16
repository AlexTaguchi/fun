# Draw fractal snowflake

import turtle
import tensorflow


def snowflake(turt, stride):
    if stride < 1.5:
        return
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


t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.up()
t.left(120)
t.forward(300)
t.right(120)
t.down()
t.width(3)
for _ in range(3):
    snowflake(t, 10)
    t.right(120)
t.right(30)
t.up()
t.forward(32)
t.down()
t.left(30)
t.width(2)
for _ in range(3):
    snowflake(t, 8)
    t.right(120)
t.right(30)
t.up()
t.forward(32)
t.down()
t.left(30)
t.width(1)
for _ in range(3):
    snowflake(t, 6)
    t.right(120)

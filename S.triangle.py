from turtle import *

def sierpinski(i, n):
    if n == 0:
        forward(i)
        left(120)
        forward(i)
        left(120)
        forward(i)
        left(120)
    else:

        sierpinski(i / 2, n - 1)
        forward(i / 2)
        sierpinski(i / 2, n - 1)
        left(120)
        forward(i / 2)
        right(120)
        sierpinski(i / 2, n - 1)
        right(120)
        forward(i / 2)
        left(120)
penup()
goto(-150, -100)
pendown()
shape("turtle")
speed('fastest')

sierpinski(300,5)
ht()
Turtle.done()



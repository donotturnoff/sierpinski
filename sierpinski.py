import turtle
import math

def top_down(origin, length):
    if length > 2:
        t.up()
        t.goto(origin)
        t.down()
        for i in range(3):
            t.fd(length)
            t.left(120)
        top_down(origin, length/2)
        top_down((origin[0] + length/2, origin[1]), length/2)
        top_down((origin[0] + length/4, origin[1] + math.sqrt( ( (length/2) ** 2 )-( ( length/4) ** 2 ) )), length/2)

def bottom_up(length, depth):
    if depth == 0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        bottom_up(length/2,depth-1)
        t.fd(length/2)
        bottom_up(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        bottom_up(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

window = turtle.Screen()
window.screensize()
window.setup(width = 1.0, height = 1.0)

t = turtle.Turtle()
t.speed(10)

length = int(input("Side length (px)? "))
origin = (-length/2, math.sqrt(3) / 2 * (-length/2))
t.up()
t.goto(origin)
t.down()

if input("Bottom-up (b) or top-down (t)? ").lower() == "b":
    bottom_up(origin, length)
else:
    top_down(length, int(input("Recursion depth? ")));

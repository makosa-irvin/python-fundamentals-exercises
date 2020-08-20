#exercise 3
    #A function that draws a polygon given no. of sides and side length
import turtle
import random
def drawPoly(n,length):
    t = turtle.Turtle()
    screen = t.getscreen()

    angle = 360 / n

    for i in range(n):
        t.left(angle)
        t.forward(length)

    t.ht()
    screen.exitonclick()

drawPoly(4,65)

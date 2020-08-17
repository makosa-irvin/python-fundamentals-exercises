#Exercise 7
    #Draw trucks of random sizes and random places
import turtle
import random

rand = random.Random()
t = turtle.Turtle ()
screen = t.getscreen ()

screen.tracer(100)


for i in range(400):
    #make diff sizes scale factor
    sizeSF = rand.uniform(0.1,1.0)
    print(sizeSF)

    #diff locations
    xLoc = rand.randint(-300,300)
    yLoc = rand.randint(-300,300)
    t.penup()
    t.goto(xLoc,yLoc)
    t.pendown()
    #draw truck
    t.fillcolor("black")
    t.begin_fill ()
    t.circle (20 * sizeSF)
    t.end_fill ()
    t.penup ()
    t.forward (120 * sizeSF)
    t.pendown ()
    t.begin_fill ()
    t.circle (20 * sizeSF)
    t.end_fill ()
    t.penup ()
    t.left (90)
    t.forward (40 * sizeSF)
    t.right (90)
    t.forward (30 * sizeSF)
    t.right (180)
    t.pendown ()
    t.fillcolor("yellow")
    t.begin_fill ()
    t.forward (180 * sizeSF)
    t.right (90)
    t.forward (30 * sizeSF)
    t.right (90)
    t.forward (90 * sizeSF)
    t.left (90)
    t.forward (30 * sizeSF)
    t.right (90)
    t.forward (30 * sizeSF)
    t.right (45)
    t.forward (43 * sizeSF)
    t.left (45)
    t.forward (30 * sizeSF)
    t.right (90)
    t.forward (30 * sizeSF)
    t.end_fill ()
    t.ht()

screen.update()
screen.exitonclick ()
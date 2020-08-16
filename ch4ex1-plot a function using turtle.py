#Exercise 1
    #Program that plots function g(x) = x**4/4 - x**3/3 - 3x**2
        #x from -20 to 20, y from -20 to 20
        #y can be found by definition of function g
import turtle
t = turtle.Turtle()
screen = t.getscreen()

#to bring the window after all is done
screen.tracer(0)
t.speed(10)
#make dots
for j in range(-350,350,10):
    for i in range(-350,350,10):
        t.penup()
        t.setpos(j,i)
        t.pendown()

        t.dot(2)

#the x and y lines
    #set color red


t.penup()
t.setpos(-350,0)
t.pendown()

t.color('red')
t.begin_fill()
t.forward(700)

t.end_fill()

    #change position for y axis
t.penup()
t.setpos(0,-350)
t.pendown()

t.color('red')
t.begin_fill()
t.left(90)
t.forward(700)

t.end_fill()

#the formula
t.color('blue')
t.pensize(2)
for x in range(-20,20):
    y = (x**4)/4 - (x**3)/3 - 3 *(x**2)
    #it is multiplied for easy visibility

    if y < 300:

        
        t.goto(x*15,y*15) #x and y are multiplied for easy visibility
        
        t.dot(5)

turtle.mainloop()
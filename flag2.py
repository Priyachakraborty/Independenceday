import turtle
from turtle import *

screen = turtle.Screen()
t = turtle.Turtle()
speed(1)

# Write "#SCALER 'INDEPENDENCE DAY' CHALLENGE "
t.penup()
t.goto(-1,300)
t.pendown()
t.color("blue")
t.write("#SCALER 'INDEPENDENCE DAY' CHALLENGE ", align="center", font=("Arial", 10, "bold"))


# Write "HAPPY 77TH INDEPENDENCE DAY"
t.penup()
t.goto(-1,210)
t.pendown()
t.color("black")
t.write("HAPPY 77TH INDEPENDENCE DAY", align="center", font=("Arial", 34, "bold"))

t.penup()
t.goto(-200, 125)
t.pendown()


t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)


t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()


t.penup()
t.goto(35, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()


t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()


t.penup()
t.goto(-27, -4)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()


t.color("navy")
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()


t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)


# Write "#HarCoderBanayeTiranga"
t.penup()
t.goto(0, -220)
t.pendown()
t.color("black")
t.write("#HarCoderBanayeTiranga", align="center", font=("Arial", 10, "bold"))

turtle.done()
import turtle
import time

t=turtle.Turtle()

t.speed(0)

t.circle(50)
t.left(180)
t.circle(100)

t.up()
t.goto(25,90)
t.down()
t.color("red")
t.begin_fill()
t.right(90)
t.forward(20)
t.left(90)
t.forward(10)
t.right(90)
t.forward(20)
t.left(90)
t.forward(30)
t.left(90)
t.forward(20)
t.right(90)
t.forward(10)
t.left(90)
t.forward(20)
t.end_fill()

t.color("gray")
t.begin_fill()
t.up()
t.goto(12,60)
t.down()
t.circle(4)
t.end_fill()

t.begin_fill()
t.up()
t.goto(-12, 60)
t.down()
t.circle(4)
t.end_fill()

t.begin_fill()
t.up()
t.goto(7, 50)
t.down()

t.color("orange")
t.forward(20)
t.left(120)
t.forward(20)
t.left(120)
t.forward(20)
t.end_fill()

t.color("black")
t.up()
t.goto(100,-90)
t.down()


t.right(90)
t.forward(100)

t.up()
t.goto(-100,-90)
t.down()


t.left(60)
t.forward(100)

t.hideturtle()
time.sleep(5)

import turtle
t=turtle.Turtle()
s=turtle.Screen()

turtle.bgcolor("black")

t.color("yellow")
t.up()
t.goto(50, 50)
t.down()
t.begin_fill()
t.circle(50, 720, 5)
t.end_fill()
# t.goto(-100, -100)

t.up()
t.goto(-50, 50)
t.down()
t.begin_fill()
t.circle(50, 720, 5)
t.end_fill()

t.up()
t.goto(-50, -50)
t.down()
t.begin_fill()
t.circle(50, 720, 5)
t.end_fill()

t.up()
t.goto(50, -50)
t.down()
t.begin_fill()
t.circle(50, 720, 5)
t.end_fill()

s.mainloop()

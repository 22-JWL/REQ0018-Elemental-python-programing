import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.speed(0)

t.up()
t.goto(-150,-150)
t.down()
t.color("red")
t.begin_fill()
t.circle(110)
t.end_fill()

t.up()
t.goto(-150,-130)
t.down()
t.color("white")
t.begin_fill()
t.circle(90)
t.end_fill()

t.up()
t.goto(-150,-110)
t.down()
t.color("red")
t.begin_fill()
t.circle(70)
t.end_fill()

t.up()
t.goto(-150,-90)
t.down()
t.color("blue")
t.begin_fill()
t.circle(50)
t.end_fill()


t.up()
t.goto(-195,-55)
t.down()
t.color("white")
t.begin_fill()
t.fd(92)
t.left(144)
t.fd(92)
t.left(144)
t.fd(92)
t.left(144)
t.fd(92)
t.left(144)
t.fd(92)
t.left(144)
t.end_fill()
t.hideturtle()

s.mainloop()

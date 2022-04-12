import turtle

t=turtle.Turtle()
s=turtle.Screen()
t.speed(5)

t.shape("turtle")
t.up()
t.goto(0,0)
t.down()
t.color("red")
t.begin_fill()
t.circle(150)
t.left(180)
t.circle(150)
t.left(90)
t.circle(150)
t.left(180)
t.circle(150)

t.end_fill()
# t.hideturtle()

t.up()
t.goto(500, 500)
t.down()
t.circle(50, 720, 3)

t.up()
t.goto(-500, 500)
t.down()
t.circle(50, 720, 4)

t.up()
t.goto(500, -500)
t.down()
t.circle(50, 720, 5)

t.up()
t.goto(-500, -500)
t.write(t.position())


s.mainloop()


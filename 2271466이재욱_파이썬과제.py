import turtle, time

t=turtle.Turtle()
t.shape("turtle")
t.circle(100) #지름 200 중앙좌표(0.100)
t.up()
t.goto(-96, 70)
t.down()

t.color("yellow")
t.begin_fill()


t.fd(192)
t.left(144)
t.fd(192)
t.left(144)
t.fd(192)
t.left(144)
t.fd(192)
t.left(144)
t.fd(192)
t.left(144)

t.end_fill()

time.sleep(5)



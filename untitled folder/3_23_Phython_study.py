import turtle

t1=turtle.Turtle() #객체생성자
t1.shape("turtle")
t1.shapesize(2)
t1.goto(-200, +100)
t1.color("magenta")
t1.right(45)
t1.position()
t1.write(t1.position())


# t2= turtle.Turtle()
# t2.shape("square")
# t2.goto(-200, -100)
# t2.shapesize(2,3)
# t2.position()
# #t2.write("         " + t1.position())
# t2.write("         " + str(t1.position()))
# t3= turtle.Turtle()
# t3.shape("circle")

# t3.penup()
# t3.goto(+200, 0)
# t3.position()
# t3.write(t3.position())
# t3.circle(50)
# t3.pendown()
# t3.circle(50)
# t3.shape("turtle")
# t3.left(180)
# t3.circle(50)
input("press any key to exit")
#터틀은 print지원 x
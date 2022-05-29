import turtle, random, time
t=turtle.Turtle()
s=turtle.Screen()
s.setup(700, 600)
turtle.colormode(255)
turtle.bgcolor(0, 0, 0)

# c=['red', 'green', 'blue', 'purple']

while True:
    # t.color(random.choice())
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    t.color(r, g, b)
    t.up()
    x=random.randint(-300, 300)
    y=random.randint(-250, 250)
    t.goto(x, y)
    t.down()


    t.begin_fill()
    반지름=random.randint(10, 50)
    t.circle(반지름, 720, 5)
    t.end_fill()
    
s.mainloop()
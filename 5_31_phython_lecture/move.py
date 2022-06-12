import turtle, random
t=turtle.Turtle(); s=turtle.Screen()
t.shape('turtle'); t.speed(0)

def 회전():
    t.left(random.randint(-180,180))

def 펜들기():
    t.up()

def 펜내리기():
    t.down()

def 이동(x, y):
    t.goto(x, y)

s.listen()
s.onkey(회전, 'c')
s.onkey(펜들기, 'Up')
s.onkey(펜내리기, 'Down')
s.onkey(t.clear, 'd')#clear()중요!

# s.onscreenclick(이동)
t.ondrag(이동)
s.mainloop()
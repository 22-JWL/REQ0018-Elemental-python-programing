import turtle, time, random
t=turtle.Turtle()
t1=turtle.Turtle()
t2=turtle.Turtle()
s=turtle.Screen()
s.setup(1800, 1400)
turtle.colormode(255)
turtle.bgcolor(200, 200, 225);

ele="/Users/jw/phython/2271466이재욱/rabbit.gif"
li="/Users/jw/phython/2271466이재욱/tiger.gif"

s.addshape(ele)
s.addshape(li)

score = 0

t.shape(ele)

t2.ht()
t1.ht()
t1.up();
t1.goto(-800, 600)
t1.write("점수 : ", font='굴림 30')


def 점수더하기():
    global score
    score = score + 1

def 점수표시():
    t2.clear()
    t2.ht()
    t2.up();
    t2.goto(-720, 600)
    t2.write(f"{score}", font='굴림 30')

def 잡기(x, y):
    점수표시()
    점수더하기()
    t.shape(li)
    time.sleep(1);
    t.ht()

    x=random.randint(-700, 700)
    y=random.randint(-550, 550)
    t.shape(ele)
    t.up(); t.goto(x, y); t.st()

t.onclick(잡기)

s.mainloop()
import turtle, random
t= turtle.Turtle(); s=turtle.Screen()
t.shape('turtle'); turtle.colormode(255); t.speed(0);
s.setup(1000 , 800)

def 별그리기(): #함수정의
    t.begin_fill()
    for a in range(5):
        t.fd(30)
        t.left(144)
    t.end_fill()

def 색고르기():
    r=random.randint(0,225)
    g=random.randint(0,225)
    b=random.randint(0,225)
    # t.color(r, g, b)
    return r, g ,b #반환값을 리스트에 담아서 반환
    

while True:
    x=random.randint(-450,450)
    y=random.randint(-350,350)
    t.up(); t.goto(x, y); t.down()

    빨, 초, 파 =색고르기()
    t.color(빨, 초, 파)
    별그리기(random.randint(10, 50))

s.mainloop()
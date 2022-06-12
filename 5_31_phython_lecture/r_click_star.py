import turtle, random
t= turtle.Turtle(); s=turtle.Screen()
t.shape('turtle'); turtle.colormode(255); t.speed(0);
s.setup(1000 , 800); turtle.bgcolor(0, 0, 0);

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

def 클릭(x, y):
    x=random.randint(-450, 450)
    y=random.randint(-350, 350)
    t.up(); t.goto(x, y); t.down()


    t.color(색고르기())
    별그리기(random.randint(10, 50))#함수 호출

s.onclick(클릭) #onclick이벤트에 처리되는 함수를 호출할 경우 x, y좌표값 전달 약속
s.mainloop()
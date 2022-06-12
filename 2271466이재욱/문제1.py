# from random import random, randrange
# import turtle
# t=turtle.Turtle()
# t=turtle.colormode(255)
# s=turtle.Screen()

# t.speed(0)
# for b in range(10, 500, 10):
#     t.pencolor(random)
#     for a in range(5):
#         t.circle(b, 360 ,5)
#         t.left(360/5)

# s.mainloop()


import turtle, random
t= turtle.Turtle(); s=turtle.Screen()
t.shape('elephant.gif'); turtle.colormode(255); t.speed(0);

def 꽃그리기(): #함수정의
    for b in range(10, 1000, 5):
        빨, 초, 파 =색고르기()
        t.color(빨, 초, 파)
        for a in range(5):
            t.circle(b, 360 ,5)
            t.left(360/5)

def 색고르기():
    r=random.randint(0,225)
    g=random.randint(0,225)
    b=random.randint(0,225)
    # t.color(r, g, b)
    return r, g ,b #반환값을 리스트에 담아서 반환
    

while True:
   
    꽃그리기()

s.mainloop()
import time
import turtle
import random

t=turtle.Turtle()
s=turtle.Screen()


img1 = "가위.gif"
img2 = "바위.gif"
img3 = "보.gif"

s.addshape(img1)
s.addshape(img2)
s.addshape(img3)

t.up()
t.goto(-215, 200)
t.color("navy")
t.write("이재욱 : 가위, 바위, 보 게임을 시작합니다.", font=("궁서", 30, "bold"))
t.goto(0,0)
time.sleep(3)

value = random.choice(['가위', '바위', '보'])


if value == '가위' :
        t.shape(img1)
elif value == '바위' :
    t.shape(img2)
else :
    t.shape(img3)

s.mainloop()

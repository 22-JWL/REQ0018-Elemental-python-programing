import turtle
turtle.bgcolor("black")#배경색
t=turtle.Turtle() #t움직임 객체생성자
s=turtle.Screen() #화면 제어 객체생성자
t.speed(0)
색상=['white', 'yellow', 'black', 'red', "green"]

t.up(); t.goto(-300, 200); t.down()
t.color(색상[4])#리스트 개념으로 접근
t.begin_fill()
for 임의변수 in range(0, 5, 1) : #콜론으로 마무리) 
    t.fd(50)
    t.left(144)

t.end_fill()

t.up(); t.goto(+300, 100); t.down()
t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.up(); t.fd(-40); t.down()
t.color("black")
t.begin_fill()
t.circle(100)
t.end_fill()


# for 임의변수 in range(0, 5, 1) : #콜론으로 마무리) 
#     t.fd(50)
#     t.left(144)

s.mainloop() #화면고정

# input("press any key to exit")
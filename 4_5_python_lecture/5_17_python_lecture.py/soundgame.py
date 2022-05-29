import turtle, random, time, winsound
t=turtle.Turtle()
s=turtle.Screen()

x=-300
for a in range(1, 21, 1):
        t.up()
        t.goto(x, 0)

    if a%3==0: #3의 배수라면♩
        t.write('la')
        winsound.Beep(300, 500)
    else:
        t.write(a, font='굴림 15')
    time.sleep(1)
    x=x+30
s.mainloop()
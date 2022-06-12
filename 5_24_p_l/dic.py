#from tkinter import font
#from pyparsing import Word
import turtle, time
t= turtle.Turtle()
s= turtle.Screen()

ani = {'호랑이':'Tiger', '사자':'Lion', '코끼리':'Elephant'}
ani['토끼'] = 'rabbit'
ani ['거북이'] = 'turtle'
ani ['상상부기'] = 'bugi'
images=['img/tiger.gif', 'img/lion.gif', 'img/elephant.gif', 'img/rabbit.gif', 'img/turtle.gif', 'img/bugi.gif']

for a in images:
    s.addshape(a)

while True:
        time.sleep(1); t.clear()
        word=turtle.textinput('한글단어입력', '호랑이, 사자, 코끼리, 토끼, 거북이, 상상부기 종료 중 선택')
        if word=='호랑이' or  word =='사자' or word =='코끼리' or word =='토끼' or word == '거북이' or word == '상상부기' or word == '종료':
            t.ht(); t.up(); t.goto(-200, 100)
            t.write(f"{word} 영어 단어는 {ani[word]}입니다.", font = '굴림 20')
            t.up(); t.goto(0, -50); t.st()
            if word=='호랑이': t.shape(images[0])
            elif word=='사자': t.shape(images[1])
            elif word=='코끼리': t.shape(images[2])
            elif word=='토끼': t.shape(images[3])
            elif word=='거북이': t.shape(images[4])
            elif word=='상상부기': t.shape(images[5])
            elif word=='종료': quit()

        else:
            t.ht(); t.up(); t.goto(-250, 100)
            t.write(f"{word} 영어 단어는 아직 준비되지 않았습니다", font='굴림 20')
            continue

s.mainloop()
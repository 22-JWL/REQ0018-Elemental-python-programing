import time
import turtle
import random

t=turtle.Turtle()
s=turtle.Screen()

img1 = "가위.gif"
img2 = "보.gif"

s.addshape(img1)
s.addshape(img2)



value = random.choice(['앞', '뒤'])

while True:
    if value == '앞' :
        t.shape(img1)
    else : 
        t.shape(img2)

    time.sleep(1)

# s.mainloop()

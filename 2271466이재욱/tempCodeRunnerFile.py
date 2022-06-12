ef 점수더하기():
    global score
    score = score + 1

def 잡기(x, y):
    점수더하기()
    t.shape(image[1])
    time.sleep(1); t.clear()
    t.ht();
    x=random.randint(-450, 450)
    y=random.randint(-350, 350)
    t.up(); t.goto(x, y);
    t.shape(image[0])


t.onclick(잡기)
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(1)

color_list=["red", "green", "blue", "gray"]

# t.color(color_list[1])
# t.stamp()
# t.fd(100)
# t.left(120)

# t.color(color_list[0])
# t.stamp()
# t.fd(100)
# t.left(120)

# t.color(color_list[2])
# t.stamp()
# t.fd(100)
# t.left(120)
# t.ht()

for r in range(0,4,1):
    t.color(color_list[r])
    t.stamp()
    t.fd(100)
    t.left(120)
    t.ht()
    

input("press any key to exit")
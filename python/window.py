import turtle

t = turtle.Turtle()
t.speed(5)
t.width(3)

for _ in range(4):
    t.forward(200)
    t.left(90)

t.up()
t.forward(100)
t.left(90)
t.down()
t.forward(200)

t.up()
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.down()
t.forward(200)

turtle.done()
import turtle
t = turtle.Turtle()
t.shape("turtle")

# triangle
def triangle(a):
  t.down()
  t.color("green")
  t.begin_fill()
  for i in range(3):
    t.forward(a)
    t.left(120)
  t.end_fill()
  t.up()

for i in range(3):
  triangle(100)
  t.right(90)
  t.forward(50)
  t.left(90)

t.forward(40)
t.color("brown")
t.down()
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.end_fill()
t.up()
t.forward(100)

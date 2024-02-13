import turtle

t = turtle.Turtle()

t.color('yellow')

t.fillcolor('yellow')
t.begin_fill()
for i in range(4):
  t.forward(200)
  t.right(90)
t.end_fill()

t.penup()
t.right(45)
t.forward(50)
t.left(45)

t.color('blue')

t.fillcolor('blue')
t.begin_fill()
for i in range(4):
  t.forward(130)
  t.right(90)
t.end_fill()

t.right(45)
t.penup()
t.forward(50)
t.left(45)

t.color('red')

t.fillcolor('red')
t.begin_fill()
for i in range(4):
  t.forward(60)
  t.right(90)
t.end_fill()

t.right(45)
t.penup()
t.forward(20)
t.left(45)

t.color('white')

t.fillcolor('white')
t.begin_fill()
for i in range(4):
  t.forward(30)
  t.right(90)
t.end_fill()

t.color('red')

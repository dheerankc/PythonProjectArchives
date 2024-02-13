#------------Modules------------|

import turtle
import random

#------------background---------|

max_speed = 1500

t = turtle.Turtle()
t.speed(max_speed)
t.penup()
t.ht()
t.color('black')

t.goto(-200,-200)

t.speed(150)
t.color('black')

t.begin_fill()

for i in range(0,4):
  t.forward(400)
  t.left(90)
  
t.end_fill()

t.color('black')

t.left(45)
t.penup()
t.forward (50)

t.begin_fill()

t.right(45)
for i in range(0,4):
  t.forward(325)
  t.left(90)
  
t.end_fill()

t.forward(65)
t.pendown()
t.color('white')

t.left(90)
t.forward(325)
t.backward(325)
t.right(90)

t.left(90)
t.forward(325)
t.backward(325)
t.right(90)
t.forward(65)

t.left(90)
t.forward(325)
t.backward(325)
t.right(90)
t.forward(65)

t.left(90)
t.forward(325)
t.backward(325)
t.right(90)
t.forward(65)

t.left(90)
t.forward(325)
t.left(90)
t.forward(195)
t.backward(195)
t.right(90)
t.backward(43)
t.left(90)
t.forward(195)
t.backward(195)
t.right(90)
t.backward(284)

t.ht()


#--------------racers----------|

r1 = turtle.Turtle()
r2 = turtle.Turtle()
r3 = turtle.Turtle()

#======racer 1=========||
r1.shape('arrow')
r1.color('yellow')

r1.penup()
r1.goto(-70,-140)
r1.left(90)

#======racer 2=========||
r2.shape('arrow')
r2.color('blue')

r2.penup()
r2.goto(-5,-140)
r2.left(90)

#======racer 3=========||
r3.shape('arrow')
r3.color('red')

r3.penup()
r3.goto(60,-140)
r3.left(90)

#-----------text code-------|

text = turtle.Turtle()
text.ht()
text.penup()
text.color('white')
text.goto(-28,170)
text.write("Go!", font =("Arial",20,"bold"))

#----------race main--------|
for i in range(120):
  r1.forward(random.randint(1,5))
  r2.forward(random.randint(1,5))
  r3.forward(random.randint(1,5))
  
  if r1.ycor() >=107:
    text.clear()
    text.goto(-55,170)
    text.write ("Yellow wins!", font =("Arial",15,"bold"))
    exit()
  elif r2.ycor() >=107:
    text.clear()
    text.goto(-50,170)
    text.write ("Blue wins!", font=("Arial",15,"bold"))
    exit()
  elif r3.ycor() >=107:
    text.clear()
    text.goto(-50,170)
    text.write ("Red wins!", font =("Arial",15,"bold"))
    exit()

 


































import turtle 

Me = turtle.Turtle()

Me.speed(100000000000000000)

for i in range(180):
    Me.forward(100)
    Me.right(30)
    Me.forward(20)
    Me.left(60)
    Me.forward(50)
    Me.right(30)
    
    Me.penup()
    Me.setposition(0, 0)
    Me.pendown()
    
    Me.right(2)
    
turtle.done()

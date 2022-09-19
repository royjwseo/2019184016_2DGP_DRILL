import turtle
turtle.shape('turtle')

def up():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)
    
def right():
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50)
    
def left():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)
    
def down():
    turtle.setheading(-90)
    turtle.stamp()
    turtle.forward(50)
    
def restart():
    turtle.reset()

turtle.onkey(up,'w')
turtle.onkey(right,'d')
turtle.onkey(left,'a')
turtle.onkey(down,'s')
turtle.onkey(restart,'Escape')
turtle.listen()


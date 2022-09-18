import turtle




pointx=0
pointy=-100
countline=0
while(countline<5):
    pointx=0
    county=0
    pointy+=100    
    turtle.penup()
    turtle.goto(pointx,pointy)
    turtle.pendown()
    while(county<5):
        countx=0
        while(countx<4):
            turtle.forward(100)
            turtle.left(90)
            countx+=1
        

        pointx+=100
        turtle.penup()
        turtle.goto(pointx,pointy)
        turtle.pendown()
        county+=1
    countline+=1     
   
    

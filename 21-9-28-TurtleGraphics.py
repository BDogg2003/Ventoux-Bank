import turtle
pen = turtle.Turtle()
pen.pencolor("gray")
pen.goto(0,300)
pen.goto(0,-300)
pen.goto(0,0)
pen.goto(300,0)
pen.goto(-300,0)
pen.pencolor("black")
pen.pensize(3)
pen.penup()
pen.goto(-100,-50)
pen.pendown()
pen.goto(-100,50)
pen.goto(-100,0)
pen.goto(-50,0)
pen.goto(-50,-50)
pen.goto(-50,50)
pen.penup()

pen.goto(50,-50)
pen.pendown()
pen.goto(50,50)
pen.goto(50,-50)
pen.circle(28,180)
pen.left(180)
pen.circle(22,180)

input("Press enter to exit")

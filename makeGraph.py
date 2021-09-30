import turtle
pen = turtle.Turtle()

def draw():
    pen.penup()
    pen.goto(-300,300)
    pen.pencolor("gray")
    pen.pendown()
    pen.speed(20)
    x = -300
    while (x<=300):
        pen.goto(x,300)
        pen.pendown()
        pen.goto(x,-300)
        x += 10
        pen.penup()

    y = -300
    while (y<=300):
        pen.goto(300,y)
        pen.pendown()
        pen.goto(-300,y)
        y += 10
        pen.penup()

    pen.pencolor("black")
    pen.goto(0,0)
    pen.pendown()
    pen.goto(320,0)
    pen.goto(-320,0)
    pen.goto(0,0)
    pen.goto(0,320)
    pen.goto(0,-320)
    pen.penup()
    pen.goto(0,0)

draw()

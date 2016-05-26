import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

def draw_square():
    leo = turtle.Turtle()
    leo.shape("turtle")
    leo.speed(2)
    leo.color("blue")

    i = 1
    while(i<=4):
        leo.forward(200)
        leo.right(90)
        i = i + 1

def draw_circle():
    raphael = turtle.Turtle()
    raphael.speed(2)
    raphael.shape("turtle")
    raphael.color("red")
    raphael.circle(150)


def draw_triangle():
    don = turtle.Turtle()
    don.speed(2)
    don.shape("turtle")
    don.color("purple")

    i = 1
    while (i<=3):
        don.forward(200)
        don.left(120)
        i = i + 1

draw_shapes()

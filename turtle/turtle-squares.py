import turtle

def draw_squares_circle():

    window = turtle.Screen()
    window.bgcolor("white")
    mike = turtle.Turtle()
    mike.speed(2)
    mike.shape("turtle")

    for j in range(1,37):
        for i in range(1,5):
            mike.forward(100)
            mike.right(90)
            print("quadrado")
        mike.right(10)

    window.exitonclick()

draw_squares_circle()

import turtle


def draw_triangle():
    turtle.color("green", "red")
    turtle.begin_fill()
    turtle.lt(60)
    for i in range(3):
        turtle.fd(200)
        turtle.rt(120)
    turtle.end_fill()


def draw_square():
    turtle.color("blue", "yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(200)
        turtle.rt(90)
    turtle.end_fill()


def draw_house():
    draw_square()
    draw_triangle()


def main():
    turtle.title("My House")
    turtle.Screen().bgcolor("lightblue")
    draw_house()
    turtle.exitonclick()


main()

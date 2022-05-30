import turtle


def draw_square():
    turtle.color("blue", "yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(200)
        turtle.rt(90)
    turtle.end_fill()


def draw_house():
    draw_square()


def main():
    draw_house()
    turtle.exitonclick()


main()

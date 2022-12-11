import turtle

turtle.title("Fractal tree")
turtle.bgcolor("#B6F5FA")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(2)
my_turtle.color("brown")
my_turtle.left(90)
my_turtle.bk(100)
my_turtle.speed(200)


def fractal_tree(n):

    if n < 10:
        return
    else:
        my_turtle.fd(n)
        my_turtle.color("green")
        my_turtle.circle(2)
        my_turtle.color("brown")
        my_turtle.left(30)
        fractal_tree(3*n/4)
        my_turtle.right(60)
        fractal_tree(3*n/4)
        my_turtle.left(30)
        my_turtle.bk(n)


fractal_tree(100)
turtle.done()






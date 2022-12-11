import turtle
import math

turtle.title("Fibonacci spiral")
factor = 1
number = int(input("Insira o número de iterações (o número deverá ser maior que 0: "))


def fibo_plot(n):
    value_a = 0
    value_b = 1

    square_a = value_a
    square_b = value_b

    my_turtle.pencolor("black")

    square_angle_b = value_b * factor
    square_angle_a = value_a * factor

    my_turtle.fd(square_angle_b)
    my_turtle.left(90)
    my_turtle.fd(square_angle_b)
    my_turtle.left(90)
    my_turtle.fd(square_angle_b)
    my_turtle.left(90)
    my_turtle.fd(square_angle_b)

    temp = square_b
    square_b += square_a
    square_a = temp

    for i in range(1, n):
        my_turtle.bk(square_angle_a)
        my_turtle.right(90)
        my_turtle.bk(square_angle_b)
        my_turtle.left(90)
        my_turtle.bk(square_angle_b)
        my_turtle.left(90)
        my_turtle.fd(square_angle_b)

        temp = square_b
        square_b += square_a
        square_a = temp

    my_turtle.penup()
    my_turtle.setposition(factor, 0)
    my_turtle.seth(0)
    my_turtle.pendown()

    my_turtle.pencolor("red")

    my_turtle.left(90)

    for i in range(n):
        print(value_b)
        fdwd = math.pi * square_angle_b / 2
        fdwd /= 90
        for j in range(90):
            my_turtle.fd(fdwd)
            my_turtle.left(1)
        temp = value_a
        value_a = value_b
        value_b += temp

        
if number > 0:
    print("Série de Fibonacci para {} elementos: ".format(number))
    my_turtle = turtle.Turtle()
    my_turtle.speed(100)
    fibo_plot(number)
    turtle.done()
else:
    print("O número de iterações deve ser maior do que zero")











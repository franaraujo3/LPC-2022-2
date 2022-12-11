import turtle
import random


#Título da tela
turtle.title("Turtle race")

#Background
turtle.bgcolor("#97CC83")

#Configuração do primeiro jogador
player_one = turtle.Turtle()
player_one.shape("turtle")
player_one.color("#25805B")
player_one.shapesize(2,2,1)
player_one.penup()
player_one.goto(-200,100)

#Configuração do segundo jogador
player_two = player_one.clone()
player_two.color("#00482B")
player_two.penup()
player_two.goto(-200,-100)

#Criação da ¨home"(ponto de chegada) de cada jogador
#Jogador 1
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

#Jogador 2
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

#Criação do dado
dice = [1,2,3,4,5,6]

#Desenvolvimento do jogo
home_position_one = (300,100)
home_position_two = (300, -100)

for i in range(20):

    if player_one.pos() >= (home_position_one):
        print("Jogador um é o vencedor!")
    elif player_two.pos() >= (home_position_two):
        print("Jogador dois é o vencedor!")
    else:
        player_one_turn = input("Digite a palavra 'ENTER' para rolar o dado: ")
        dice_outcome = random.choice(dice)
        print("O resultado é: {}".format(dice_outcome))
        steps = 20*dice_outcome
        print("O número de passos será: {} passos".format(steps))
        player_one.fd(steps)
        player_two_turn = input("Digite a palavra 'ENTER' para rolar o dado: ")
        dice_outcome = random.choice(dice)
        print("O resultado é: {}".format(dice_outcome))
        steps = 20 * dice_outcome
        print("O número de passos será: {} passos".format(steps))
        player_two.fd(steps)




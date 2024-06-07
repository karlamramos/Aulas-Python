#DESAFIO 01

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 5 e 0 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
print("")
print("**JOGO DO ADIVINHE O NÚMERO**")
print("")
numerousuario= int(input("Digite um número entre 0 a 5: "))
print("")
numerocomputador = random.randint(0,5)
print (f"Numero escolhido PC: {numerocomputador}")

if numerousuario==numerocomputador:
    print("Parabéns, você venceu :) !")
else:
    print("Que peninha, você perdeu :( !")

import random

while True:
    print("")
    print("**JOGO DO ADIVINHE O NÚMERO**")
    print("")
    numerousuario= int(input("Digite um número entre 0 a 5: "))
    print("")
    numerocomputador = random.randint(0,5)
    print (f"Numero escolhido PC: {numerocomputador}")
    print ('---------------------------------')

    if numerousuario==numerocomputador:
        print("Parabéns, você venceu 👍👏!")
        print ('---------------------------------')
    else:
        print("Que peninha, você perdeu 👎😐 !")
        print ('---------------------------------')
    resposta= input("Deseja sair? (s/n):")
    if resposta.lower() =='s':
        print ('')
        print("Obrigado por jogar.")

        break
    #print ("Continue o loop...")
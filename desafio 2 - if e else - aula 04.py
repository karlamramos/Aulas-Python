# DESAFIO 02

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade= float(input("Digite a velocidade do carro (km/h): "))
limite = 80
multaporkm = 7.00

if velocidade>limite:
    excesso = velocidade-limite
    multa= excesso*multaporkm
    print(f"Você foi multado!")
    print (f" A multa vai custar {multa} reais !")
else:
    print(f" ok - velocidade permitida !!")
    
print ('Fim')
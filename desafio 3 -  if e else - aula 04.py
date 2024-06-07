#DESAFIO 03

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

distanciadaviagem= float(input("Informe a distancia da viagem em (km/h):"))

valorporkmde200 = 0.50
valorporkmmaislonga = 0.45

if distanciadaviagem<=200:
    valor1 = distanciadaviagem*valorporkmde200
    print(f"O valor da sua viagem é de {valor1} reais!")
else:
    valor2= distanciadaviagem*valorporkmmaislonga
    print (f"O valor da sua viagem é de {valor2} reais!")


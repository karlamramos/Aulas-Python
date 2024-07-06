#Versão 1 - Calculadora de IMC

peso=float(input("Digite seu peso em (kg): "))
altura= float(input("Digite sua altura em (metros): "))

IMC = peso / (altura ** 2)

print ("Seu IMC é %.1f" %IMC)

#Tabela Padrão:
#Abaixo do peso para imc abaixo de 18,5
# normal se o imc estiver entre 18,5 e 24,9:
#Sobrepeso se o imc estiver entre 25 e 29,9
#Obesidade para imc maior que 29,9

if IMC<=18.5:
    print ("você está abaixo do peso")

elif IMC<=24.9:
    print("Você está com o peso normal")

elif IMC<=29.9:
    print("Você está com sobrepeso!")

else:
    print("Obesidade !!!")
#Versão 2 - Calculadora de IMC

print("Calculadora de IMC")
print("")

total_analises = 0
abaixo_peso = 0
peso_normal = 0
sobrepeso = 0
obesidade = 0

while True:
    try:
        peso=float(input("Digite seu peso em (kg): "))
        altura= float(input("Digite sua altura em (metros): "))
        IMC = peso / (altura ** 2)

        if IMC < 18.5:
            classificacao = "Abaixo do peso"
            abaixo_peso += 1
        elif 18.5 <= IMC < 25:
            classificacao = "Peso normal"
            peso_normal += 1
        elif 25 <= IMC < 30:
            classificacao = "Sobrepeso"
            sobrepeso += 1
        else:
            classificacao = "Obesidade"
            obesidade += 1

        total_analises += 1

        print(("Seu IMC é %.1f" %IMC))
        (f" Você está com ({classificacao})")

        continuar = input("Deseja fazer outra análise? (s/n): ")
        if continuar.lower() != "s":
            break

    except ValueError:
        print(" Insira valores numéricos válidos !!")

print("\nEstatísticas:")
print(f"Total de análises feitas: {total_analises}")
print(f"Abaixo do peso: {abaixo_peso} ({(abaixo_peso / total_analises) * 100:.2f}%)")
print(f"Peso normal: {peso_normal} ({(peso_normal / total_analises) * 100:.2f}%)")
print(f"Sobrepeso: {sobrepeso} ({(sobrepeso / total_analises) * 100:.2f}%)")
print(f"Obesidade: {obesidade} ({(obesidade / total_analises) * 100:.2f}%)")
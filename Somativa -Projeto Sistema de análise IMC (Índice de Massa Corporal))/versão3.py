import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(345,550)

#Versão 2 - Calculadora de IMC

print("Calculadora de IMC")
print("")


1

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def exibir_estatisticas(total_analises, abaixo_peso, peso_normal, sobrepeso, obesidade):
    print(f"Total de análises feitas: {total_analises}")
    print(f"Abaixo do peso: {abaixo_peso} ({(abaixo_peso / total_analises) * 100:.2f}%)")
    print(f"Peso normal: {peso_normal} ({(peso_normal / total_analises) * 100:.2f}%)")
    print(f"Sobrepeso: {sobrepeso} ({(sobrepeso / total_analises) * 100:.2f}%)")
    print(f"Obesidade: {obesidade} ({(obesidade / total_analises) * 100:.2f}%)")

def main():
    total_analises = 0
    abaixo_peso = 0
    peso_normal = 0
    sobrepeso = 0
    obesidade = 0

    while True:
        print("Digite 1 - Calculadora de IMC")
        print("Digite 2 - Verificar análise dos dados: Mostra as porcentagens")
        print("Digite 3 - Sair")

        opcao = input(" ")

        if opcao == "1":
            try:
                peso=float(input("Digite seu peso em (kg): "))
                altura= float(input("Digite sua altura em (metros): "))
                IMC = calcular_imc(peso, altura)
                classificacao = classificar_imc(IMC)
                print('')
                print(("Seu IMC é %.1f" %IMC))
                print(f"Você está com ({classificacao})")
                print('')

                if classificacao == "Abaixo do peso":
                    abaixo_peso += 1
                elif classificacao == "Peso normal":
                    peso_normal += 1
                elif classificacao == "Sobrepeso":
                    sobrepeso += 1
                else:
                    obesidade += 1

                total_analises += 1

            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
        elif opcao == "2":
            exibir_estatisticas(total_analises, abaixo_peso, peso_normal, sobrepeso, obesidade)

        elif opcao == "3":
            break

        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()

janela.show()
app.exec()
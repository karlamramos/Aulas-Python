import random

vitorias_consecutivas = 0

while True:
    jogador = int(input("Digite um número (0 para parar): "))
    computador = random.randint(1, 10)  # Escolhe um número aleatório entre 1 e 10

    total = jogador + computador
    escolha = input("Par ou ímpar? (P/I): ").strip().lower()

    if (total % 2 == 0 and escolha == 'p') or (total % 2 != 0 and escolha == 'i'):
        print(f"Você ganhou! O computador escolheu {computador}.")
        vitorias_consecutivas += 1
    else:
        print(f"Você perdeu! O computador escolheu {computador}.")
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")
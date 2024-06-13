# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores

soma = 0
quantidade = 0
maior = float('-inf')
menor = float('inf')

while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    soma += n
    quantidade += 1
    maior = max(maior, n)
    menor = min(menor, n)

media = soma / quantidade

print("Quantidade de números digitados:", quantidade)
print("Soma:", soma)
print(f"Média: {media:.2f}")
print("Maior valor:", maior)
print("Menor valor:", menor)
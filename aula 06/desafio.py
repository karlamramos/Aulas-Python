# DESAFIO 02

# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999).

soma = 0
quantidade = 0

while True:
    numerointeiro = int(input("Digite um número inteiro: "))
    if numerointeiro == 999:
        break
    soma += numerointeiro
    quantidade += 1

print("Quantidade de números digitados:", quantidade)
print("Soma:", soma)
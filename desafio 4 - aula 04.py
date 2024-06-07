#DESAFIO 04
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1= int(input("Digite um número inteiro:"))
num2= int(input("Digite um número inteiro:"))
num3= int(input("Digite um número inteiro:"))

maiornumero = max(num1,num2,num3)
menornumero = min(num1,num2,num3)

print (f"O maior numero é: {maiornumero}")
print (f"O menor número é: {menornumero}")


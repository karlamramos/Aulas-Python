# #DESAFIO 02

# Crie um programa que leia o nome de uma cidade e siga se ela
# começa ou não com o nome “Santo”.

cidade = (input("Digite o nome da sua cidade: "))
dividenomedacidade = cidade.split ()
print (dividenomedacidade)

primeironomedacidade=dividenomedacidade[0].upper()
print (primeironomedacidade)

verificaprimeirapalavra = "SANTO" in primeironomedacidade

print (f"O nome da cidade {cidade} começa com santo: {verificaprimeirapalavra}")
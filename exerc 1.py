#Crie um programa que leia o nome completo de uma pessoas e mostre

# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input("Digite o seu nome completo: "))
nomeupper = nome.upper ()
nomelower = nome.lower ()
print (nomeupper)
print (nomelower)

nomesemespaco= nome.replace (" ","")
print (nomesemespaco)
print (f"seu nome possui : {len(nomesemespaco)} letras")

divideTexto = nome.split ()
print (f "seu primeiro nome possui:" (len(divideTexto[0]))
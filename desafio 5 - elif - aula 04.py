# Media escola

# Aprovado se  media maior ou igual a 7
# faltas até 10

nota= int(input("Digite a nota do aluno:"))
faltas= int(input("Digite a quantidade de faltas do aluno:"))
media =7

if nota<media:
    print(f"Você foi reprovado !")
elif faltas >=10:
    print(f"Você foi reprovado !")
else: 
    nota>media
    print(f"Você foi aprovado !")

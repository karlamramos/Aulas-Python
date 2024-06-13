#DESAFIO SENHA

# nome = input("Digite seu nome de usuário: ")
# senha = input("Digite sua senha: ")

# while nome == senha:
#     print("Erro: A senha não deve ser igual ao nome.")
#     senha = input("Digite uma nova senha: ")

# print("Login Ok")

#   WHILE

# x = int(input("digite um numero inteiro: "))
# y = int(input("digite um numero inteiro: "))

# while x<=10:
#     print(x)
#     # x=x+1
#     x+=y
# else:
#     print ("fim")

numero=0

# while numero <5:
#     numero +=1
    
#     if numero ==3:
#         print ("Vamos pular a interação para",numero)
#         continue
        
#     print ("numero:", numero)

while True:
    resposta= input("Deseja sair? (s/n):")
    if resposta.lower() =='s':
        print("Saindo do loop.")
        break
    print ("Continue o loop...")
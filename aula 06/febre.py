qnt_analisadas= int(input("Quantas pessoas deseja analisar ? "))
print ("--------------------------------------")
fim= qnt_analisadas+1
somatoria=0

for i in range(1,fim):
    # print(i)
    temperatura= int(input("Digite  a temperatura: (°C)"))
    somatoria2= somatoria+temperatura
    
    if temperatura<=37.2:
        print("Temperatura normal😊")
        print ("--------------------------------------")
    elif temperatura>37.2 and temperatura<=38:
        print("Temperatura febril😢")
        print ("--------------------------------------")
    elif temperatura>38 and temperatura<=39:
        print("Está com febre🤒")
        print ("--------------------------------------")
    else:
        print ("Está com febre alta🥵")
        
        print ("--------------------------------------")
        
media= somatoria2/qnt_analisadas
print= (f"Média de temperatura de {qnt_analisadas} pessoas = {media}")

while True:
    resposta= input("Deseja sair? (s/n):")
    if resposta.lower() =='s':
        print("Saindo do loop.")
        break
    print("Continue o loop...")
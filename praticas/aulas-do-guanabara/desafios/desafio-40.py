#Jogo da adivinhação (agora contando as tentativas).

import random


numeros = [1,2,3,4,5]
digitado =0
sorteio = random.choice(numeros)
contador = 0

while digitado != sorteio :
    
    digitado = int(input("Digite um número : "))

    if digitado != sorteio:
        print("Tente de novo ")
    
    contador +=1
    
    if  digitado == sorteio:
        print(f"O número sorteado é : {sorteio}")
        print(f"O número de tentativas foi {contador}")
    
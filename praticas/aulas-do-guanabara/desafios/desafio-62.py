"""Leia cinco números e armazene-os em uma lista. Mostre o maior e o menor valor e suas posições."""


lista = []
maior = 0
menor = 1000

for i in range(5) :
    
    num = int(input("Digite um número : "))
    lista.append(num)
    if(num > maior):
        maior = num
        posicaomaior=i
    if num < menor:
        menor = num
        posicaomenor=i
print(lista) 
print(f"Maior número: {maior} sua posiçaõ é : {posicaomaior}")
print(f"Menor número:  {menor} sua posição é : {posicaomenor}")
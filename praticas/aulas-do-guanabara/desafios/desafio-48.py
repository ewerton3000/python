"""Leia vários números inteiros. O programa deve parar quando o usuário digitar 999. No final, mostre: 
Quantos números foram digitados (desconsiderando o 999).
A soma entre eles."""

contador = 0
while True:
    numero  = input("Numero : ")

    if numero == "999": 
        break

    contador +=1


print(f"Número de vezes que foi digitado : {contador}")

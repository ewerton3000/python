"""Leia números e crie uma lista geral, outra com os pares e outra com os ímpares."""

listapar = []
listaimpar = []
lista = []

while True:
    
    num=int(input("Digite um número  ou digite -1 para finalizar: "))

    if num == -1:
        break

    if num % 2 == 0:
        listapar.append(num)
        lista.append(num)
    
    if num % 2 == 1:
        listaimpar.append(num)
        lista.append(num)
print(f"Os números digitados foram : {lista}")
print()
print(f"Os números pares são : {listapar}")
print()
print(f" Os números impares são : {listaimpar}")
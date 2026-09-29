"""Crie uma tupla preenchida com 5 números aleatórios.

Depois mostre:

Os números gerados.
O maior.
O menor."""

tupla = (65, 82 ,855 ,78,2)
maior = tupla[0]
menor = tupla[0]
print(f"Numeros da tupla : {tupla}")
print()
print()
for  i in tupla:
    if i > maior:
        maior = i

    if i < menor:
        menor = i
print()
print()

print(f"O maior número é : {maior}")
print()
print()
print(f"O menor número é : {menor}")
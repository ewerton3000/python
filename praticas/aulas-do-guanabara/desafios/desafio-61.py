"""Leia 4 números pelo teclado.

Guarde-os em uma tupla.

Depois mostre:
Quantas vezes apareceu o número 9.
Em que posição apareceu o primeiro 3.
Quais foram os números pares."""

tupla=(9,9,7,4,2,6,3)
nove = 0
par =[]
for i in tupla:

    if i % 2 == 0:
    
        par.append(i)

    if i == 9:
     nove+=1
          

print(f"Os números pares são : {par}")
print()
print()
print()
print(f'O número 3 está na {tupla.index(3)}°  posição da tupla')
print()
print()
print()
print(f"O número 9 apareceu {nove} vezes")
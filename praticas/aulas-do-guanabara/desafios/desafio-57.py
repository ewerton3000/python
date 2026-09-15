"""Crie uma tupla com cinco números aleatórios e mostre o maior e o menor."""

numeros=(40,50,1,80,100)
maior = numeros[0]
menor = numeros[0]
for i in numeros:

    
    if i >maior:
        maior = i
     
    elif i <menor:
        menor= i


print(f"O maior valor é  {maior}")
print(f"O menor valor é {menor}")


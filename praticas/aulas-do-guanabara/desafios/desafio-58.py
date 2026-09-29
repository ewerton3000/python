"""Leia quatro valores e armazene-os em uma tupla. Depois, faça algumas análises sobre esses valores."""

numeros = (2,4,9,7)


numpar = []
numimpar = []
for  i in numeros:
        if i % 2 == 0:
            numpar.append(i)
        
        if i % 2 == 1:
            numimpar.append(i)
print(f"Os números pares são {numpar}")
print(f"Os números impáres são {numimpar}")



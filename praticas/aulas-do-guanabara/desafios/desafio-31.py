"""Calcule a soma de todos os números ímpares que são múltiplos de 3 no intervalo de 1 até 500."""

numeros = 0
soma =0
multiplos=[]

for  numeros in range(1,501):
    if numeros % 3 == 0 and numeros %2 == 1:
        multiplos.append(numeros)
        soma=soma+numeros

print("Os números nultiplos de 3 são :  ",multiplos)
print("A soma dos números é : ",soma)
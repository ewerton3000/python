"""Mostre todos os números pares entre 1 e 50."""

par = []
impar = []
contador = 0

for numeros in range(0, 51):
    if numeros % 2 == 0:
        contador +=1
        par.append(numeros)
    else:
        impar.append(numeros)
        
print("Os números pares são: ",par)
print("Os números impares são : ",impar)
print("A contagem de números pares foi de :  ",contador)

#OBS: Observe a posição do print para o for não imprimir varias vezes até terminar o loop
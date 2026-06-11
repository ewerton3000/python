#Crie um programa que leia um número e mostre:
#O dobro
#O triplo
#A raiz quadrada

import math


num = int(input("Digite um número : "))
dobro = 2 * num
triplo = 3* num
raiz = math.sqrt(num)
print("numero digitado : {}".format(num))
print("dobro{} , triplo{}  , raizquadrada{}".format(dobro,triplo,raiz))
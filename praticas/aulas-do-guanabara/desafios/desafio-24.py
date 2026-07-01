#Leia um número real e mostre sua parte inteira.
import math

numero = float(input("Digite um número real: "))
parte_inteira = math.trunc(numero)

print(f"A parte inteira é {parte_inteira}")
"""Melhorar o exercício anterior permitindo mostrar mais termos da PA."""


contador = 1
a1 = float(input("Primeiro termo (a1):  "))
r = float(input("Número da Razão:  "))
while contador <=10:
    print(f"Razão : {a1}")
    a1 +=r
    contador +=1
    
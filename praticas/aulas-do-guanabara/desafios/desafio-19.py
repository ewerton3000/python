#Leia um número e informe se ele é positivo, negativo ou zero.

numero = int(input("Digite um número : "))

if numero >0:
    print("Positivo {}".format(numero))
elif numero <0:
    print("Negativo {}".format(numero) )
else:
    print("Neutro {}".format(numero))
""" Leia dois números e mostre qual é o maior.
Se forem iguais, informe isso."""

numero1= int(input("Digite um número : "))

numero2 = int(input("Digite outro número : "))

if numero1 > numero2:
    print("O número {} é maior que o número {}".format(numero1,numero2))
elif numero2 > numero1:
    print("O número {} é maior que o número {}".format(numero2,numero1))


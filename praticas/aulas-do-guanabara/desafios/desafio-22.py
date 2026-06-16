"""Leia um número inteiro e informe se ele é:
Par
Ímpar
Dica: use o operador %."""

num = int(input("Digite um número : "))

resto = num % 2 
if resto == 0: 
    print("Par")
else:
    print("Impar")
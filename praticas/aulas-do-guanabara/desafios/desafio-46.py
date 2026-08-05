"""Ler vários números e parar usando uma sentinela."""

numeros = []

while True:
    valor = float(input("Digite um número (ou 0 para parar) : "))

    if valor == 0:
        break

    numeros.append(valor)

print(f"Você digitou os seguintes números:  {numeros}")
print(f"A soma dos números é: {sum(numeros)}")
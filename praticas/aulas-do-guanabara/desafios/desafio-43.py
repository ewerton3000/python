"""Gerar os 10 primeiros termos de uma Progressão Aritmética usando while."""

termo_atual = int(input("Digite o primeiro termo : "))
razao = int(input("Digite a razão: "))

contador = 1

while contador <=10:
    print(f"Termo {contador}: {termo_atual}")
    termo_atual += razao
    contador +=1

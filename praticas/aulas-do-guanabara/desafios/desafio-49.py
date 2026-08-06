"""Faça um programa que mostre a tabuada de vários números, um de cada vez.

O programa deve ser interrompido quando o usuário digitar um número negativo."""
numero = 1
tabuada = int(input("Digite a tabuada : "))
while True:
    
    print(f"{tabuada} x {numero}  = {tabuada * numero}")
    numero +=1

    if numero >10 :
        tabuada = int(input("Digite a tabuada : "))
        numero = 1

    elif tabuada <0 :
        print("ENCERRADO")
        break
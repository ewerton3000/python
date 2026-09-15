"""Leia quatro valores e armazene-os em uma tupla. Depois, faça algumas análises sobre esses valores."""

numeros = (2,4,9,7)

opcao = int(input("Escolha uma opção:    " \
"1 - Mostrar os números pares da TUPLA:    " \
"2 - Mostrar os números ímpares da TUPLA:    "))

match opcao:

    case 1:
        num = []
        for  i in numeros:
            if numeros % 0:
                numeros.append(num)
        print(f"Os números pares são {num}")

    case 2:
        num = []
        for  i in numeros:
            if numeros % 1:
                numeros.append(num)
        print(f"Os números impáres são {num}")

    case _:
        print("Opção inválida! Tente novamente ")
        
    
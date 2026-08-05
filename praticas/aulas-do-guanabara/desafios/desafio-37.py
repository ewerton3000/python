"""Leia o ano de nascimento de sete pessoas e informe quantas são maiores de idade e quantas são menores de idade."""

import time

ano  = time.localtime().tm_year

maiores = []
menores = []
for i in range(0,6):
    nas = int(input("Digite o anoem que vc nasce :  "))
    if nas>ano:
        print("Erro digite outro ano")
        break
    resul = ano - nas
    if resul >=18:
        maiores.append(nas)
    else:
        menores.append(nas)

print(f"Os maiores de idade nasceram nos anos: {maiores} \n Os menores de idade nasceram nos anos : {menores} ")

#Use mais este formato de f-string
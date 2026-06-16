"""Leia um nome.
Se o nome for "Ewerton", mostre uma mensagem personalizada.
Caso contrário, mostre uma saudação comum."""

nome= input("Digite um nome : ")

if nome == "Wesker" or nome =="Mario" or nome == "Zelda" or nome == "Diddy":
    print("MUITO BOM TE CONHECER {}".format(nome))
else:
    print("OLA FULANO")
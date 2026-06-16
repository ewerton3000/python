#Leia uma frase e informe se ela contém a palavra:

"""frase1 = "Eu quero programar em python"

frase2 = "Eu quero programar em php"

print(frase1.find("python"))

print(frase2.find("python"))
"""
#ou

frase = input("digite uma frase : ")
palavra =input("Digite uma palavra : ")

if palavra.lower() in frase.lower():
    print("A palavra {}  foi encontrada na frase".format(palavra))
else:
    print("A palavra {} não foi encontrada nesta frase".format(palavra))
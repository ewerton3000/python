"""Validação de sexo (M ou F)."""

sexo = input("Digite o seu sexo : ")

while sexo =="masculino":
    print("Masculino")
    break


if sexo =="feminino":
    print("feminino")

else:
    print("Por favor digite o sexo masculino ou feminino")
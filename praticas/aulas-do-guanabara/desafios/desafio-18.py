#Leia a idade de uma pessoa e informe se ela é maior ou menor de idade.

idade = int(input("Digite a sua idade "))

if idade >=18:
    print("Você tem {} anos então você é maior de idade".format(idade))
else:
    print("Você tem {} anos então você é menor de idade".format(idade))
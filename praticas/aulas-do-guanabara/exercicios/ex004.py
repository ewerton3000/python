#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todos as informações possíveis sobre ele.

algo  = input('Digite algo:  ')

print('O tipo primitivo desse valor é ',type(algo))
print('Só tem espaços?', algo.isspace())
print("É um número?",algo.isnumeric())
print("É alfabeto",algo.isalpha())
print("É alfanumerico",algo.isalnum())
print("Está em maisúculo",algo.isupper())
print("Está  minusculo",algo.islower())
print("Está capitalizada",algo.istitle())
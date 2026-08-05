#Leia o peso de cinco pessoas e informe qual é o maior e o menor peso.

from time import sleep

pesos = []
for i in range(0,5):
    peso = float(input("Digite o seu peso :  "))
    sleep(2)
    pesos.append(peso)
    
organizados = sorted(pesos,reverse=True)
maiorpeso= organizados[0]
menorpeso= organizados[-1]
pesomedio=organizados[(int(len(organizados)/2))]
print(organizados)
print(f"O maior peso é : {maiorpeso} \n  O menor peso é : {menorpeso} \n o peso medio é : {pesomedio}")
"""Faça uma contagem regressiva de 10 até 0, 
com uma pausa de 1 segundo entre cada número. Ao final, exiba uma mensagem de estouro de fogos."""

import time

for segundos in range(10,-1,-1):
    print(segundos)
    time.sleep(1)
    
    if segundos ==0:
        print("Estouro de fogos! 🎆🎇")
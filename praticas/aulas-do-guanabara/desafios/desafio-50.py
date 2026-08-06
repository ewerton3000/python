"""Faça o jogo Par ou Ímpar contra o computador.

O programa deve continuar até que o jogador perca, mostrando ao final quantas vitórias consecutivas ele conseguiu."""
import random
vitorias = 0
while True:
    apostajogador = input("Par ou impar :  ")

    if apostajogador =="impar":
        apostaaleatorio = "par"
        player= "Você"
        escolha="CPU"
    else:
        apostaaleatorio ="impar"
        player= "Você"
        escolha="CPU"

    jogador = int(input("Digite um número : "))
    aleatorio = random.randint(0 , 100)
    print(f"A cpu jogou o número :  {aleatorio}")
    resul = jogador+aleatorio 
    print(f"O resultado é  :  {resul}")
    
    if resul % 2 == 0  and apostaaleatorio == "par":
        print("Vencedor : CPU ")
        print("Finalizando o programa")
        print(f"Numero de vitórias do jogador : {vitorias}")
        break

    elif resul % 2 == 0  and apostajogador == "par":
        print("Vencedor : Jogador")
        vitorias +=1

    elif resul %2 == 1 and apostaaleatorio =="impar":
        print("Vencedor : CPU")
        print("Finalizando o programa")
        print(f"Numero de vitórias do jogador : {vitorias}")
        break

    elif resul %2 == 1 and apostajogador =="impar":
                print("Vencedor : Jogador")
                vitorias +=1

    else:
         print("Tente novamente")
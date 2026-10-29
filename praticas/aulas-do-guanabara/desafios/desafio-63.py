"""Leia vários números, evitando adicionar valores repetidos. Permita que o usuário decida quando parar."""
lista=[]
while True:
    
    num = input("Digite um número ou fim para parar : ")
    
    if num.lower() == "fim":
        break
    
    if num in lista :
        print(f"O número {num} se repete na lista ")

    else:
        lista.append(num)
        

print(lista)
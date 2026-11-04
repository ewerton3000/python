"""Leia vários números e apresente informações como quantidade de valores,
   ordem decrescente e se determinado valor foi digitado."""

lista=[]

while True:
    num = input("Digite um número: ")

    if num.lower() == "fim":
        break

    try:
        list = int(num)
        lista.append(list)

    except:
        print("Por favor, digite um número válido")

lista.sort(reverse=True)

print("\nLista em ordem decrescente: ")
print(lista)
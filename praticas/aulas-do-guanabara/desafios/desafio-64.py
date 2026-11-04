"""Leia números e insira cada um na posição correta, 
mantendo a lista ordenada sem utilizar a ordenação automática para resolver o problema."""

lista =[]

for _ in range(5):
    num = int(input("Digite um número : "))

   

    if not lista or num >= lista[-1]:
        lista.append(num)

    else:

        for i in range(len(lista)):
            if num <= lista[i]:
                lista.insert(i, num)
                break

print(f"Lista ordenada final :  {lista}")



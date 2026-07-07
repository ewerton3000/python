#Leia um número inteiro e informe se ele é primo.

n = int(input("Digite um número para ver se é primo:  "))

for n in range(1):
        if n % 1 == 0 and n % n == 0:
                print("É numero primo")
        else:
                print("Não é primo")
#Leia um número inteiro e informe se ele é primo.


n = int(input("Digite um número para ver se é primo:  "))
primo = True
if n <2:
        primo = False
for num in range(2,n):
        if n % num == 0  :
                primo = False
                break

print(primo)
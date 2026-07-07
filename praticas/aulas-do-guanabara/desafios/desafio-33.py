#Leia seis números inteiros e mostre a soma apenas dos números pares.

soma = 0
for num in range(1,7):
        num = int(input(" Digite um número: "))

        if num % 2 == 0 :
            soma=soma +num

print("A soma foi {}".format(soma))

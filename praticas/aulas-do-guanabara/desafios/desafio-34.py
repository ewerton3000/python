#Mostre os 10 primeiros termos de uma Progressão Aritmética (PA).

array=[]
vez=int(input("Digite o numero inicial dos números"))
razao = int(input("Digite a razão dos números: 1 , 2 , 3"))
for num in range(10):
            array.append(vez)
            vez = vez+razao

print(array)
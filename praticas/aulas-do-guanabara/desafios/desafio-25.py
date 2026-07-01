#Leia um número e calcule sua raiz quadrada.

from  math import sqrt,ceil,floor,pow

num = int(input("Digite um número : "))

quadrada =  pow(num,2)

raiz = sqrt(num)

cima = ceil(num)

baixo = floor(num)


print("A raiz quadrada de {} é : {} , arrendodada pra cima é {} e arredondada para baixo é : {}".format(num,raiz,cima,baixo))


#Mostre a tabuada de um número informado pelo usuário.

multiplicador = int(input("Digite o valor da tuabada que será exibida: "))
numero = 1

for numero in range(1, 11):
        resul = multiplicador * numero
        print("{} x {} = {}".format(multiplicador,numero,resul))
        
        if numero >=10:
                break
        
        numero+=1


"""Sequência de Fibonacci."""

fn1 = 1
limite = int(input("Digite até aonde a sequencia pode terminar : "))
array = []
soma = 0
while  soma <=limite:
    array.append(soma)

    proximo = soma + fn1
    soma = fn1
    fn1 = proximo
    print(array)
    
        
    
   
"""Simule um caixa eletrônico. O programa deve informar a quantidade mínima de cédulas para um determinado valor de saque."""

saldo = 1000
quantmin = [100,50,20,10]
quant=[]
contador= []
saque = 0
while True:
    print(f"Valor do saldo :  {saldo}")
    
    saque = int(input("Digite o valor que você quer sacar : "))

    for d in quantmin:
        quantidade = saque // d
        resto = saque % d

        print(f"As cedulas sacadas serão {resto} de notas de {quantidade}")
        print(f"")

        


       


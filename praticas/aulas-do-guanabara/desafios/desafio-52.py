"""Simule uma loja. Leia o nome e o preço de vários produtos.

Ao final, informe:

O total gasto na compra.
Quantos produtos custam mais de R$ 1000.
Qual é o produto mais barato."""

nome =""
nomes = []
total = 0
maisdemil = []
produtobarato = []
preco = 0
produtos =[]
while True:

    nome =input("Digite o nome do produto :  ")
    nomes.append(nome)
    preco = float(input("Digite o valor do produto : "))

    produtos.append({"nome":nome,"preco":preco})
    total = total + preco   


    c = input("Deseja continuar ?  ")
    if preco > 1000:
        maisdemil.append({"nome":nome,"preco":preco})
        


    if c in ("nao" , "n"):
                break
  
    

  
produtobarato = min(produtos, key=lambda x : x["preco"])
print(f"O total gasto na compra é :   {total}  ")
print(f"Os produtos que custaram mais de 1000 R$ foram : {maisdemil} e contado foram : {len(maisdemil)}")
print( f"O produto mais barato é: {produtobarato['nome']} " f"e custa R$ {produtobarato['preco']:.2f}" )
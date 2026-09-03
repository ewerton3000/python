"""Simule um caixa eletrônico. O programa deve informar a quantidade mínima de cédulas para um determinado valor de saque."""


saques = [80, 150]


cedulas = [50, 20, 10]

for valor_total in saques:
    print(f"\n--- Processando saque de R$ {valor_total} ---")
    valor_restante = valor_total
    
    for cedula in cedulas:

        quantidade = valor_restante // cedula
        
        valor_restante = valor_restante % cedula
        
        if quantidade > 0:
            print(f"Entregar {quantidade} nota(s) de R$ {cedula}")

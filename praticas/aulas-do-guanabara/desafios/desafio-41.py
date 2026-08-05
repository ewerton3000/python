#Criar um menu de operações com while.

dinheiro = 1000

while True:
    print("\n===== MENU ======")
    print("1 -Ver saldo")
    print("2 -Sacar")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção:  "))

    if opcao == 1:
        print(f"Seu saldo é R$ {dinheiro:.2f}")

    elif opcao == 2:
        saque = float(input("Digite o valor do saque:  "))

        if saque <= dinheiro:
            dinheiro -= saque
            print(f"Saque realizado com sucesso! ")
            print(f"Novo saldo: R$  {dinheiro:.2f}")
            
        else:
            print("Saldo insuficiente! ")

    elif opcao == 3 :
        print("Encerramento o programa...")
        break

    else:
        print("Opção inválida")
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0.00
limite = 500.00
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                ##Append do valor do saque no extrato para manter todos registrados. 
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))

            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                ##Append do valor do saque no extrato para manter todos registrados.
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        if extrato:
            for linha in extrato:
                print(linha)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

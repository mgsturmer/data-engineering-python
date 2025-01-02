menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato:
            for linha in extrato:
                print(linha)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
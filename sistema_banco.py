
menu = ("""
    ########## Modelo sistema bancario V 1.0 ##########
    
                            OPCÔES   
    [d] Depositar
    [s] Sacar
    [e] extrato
    [q] Sair
    """)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor >= 0:
            saldo += valor
            extrato += f"Deposito no valor de: R$ {valor:.2f}\n"
        else:
            print("Não são aceitos valores negativos! Refaça a operação!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saque não permitido! saldo insuficiente, seu saldo é: ", saldo)

        elif excedeu_limite:
            print(
                "Saque não permitido! Valor limite excedido.\nSeu limite é: ", limite)

        elif excedeu_saques:
            print(
                "Saque não permitido! Atingiu o limite diário de saques.\n O limite de saques é : ", LIMITE_SAQUES)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================= extrato ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "q":
        print("Agradecemos a sua visita")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

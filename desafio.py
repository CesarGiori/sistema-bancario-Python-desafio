menu = """
###Menu de Operações###

    [1] Depositar
    [2] Sacar
    [3] Transferência/PIX
    [4] Extrato
    [0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUES_DIARO = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = int(input("Informe o valor para depósito: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito : R$ {valor:.2f}\n"
            print("Operação concluida com sucesso!")

        else:
            print("Infome um valor válido! Operação cancelada.")

    elif opcao == "2":
        valor = int(input("Informe o valor para saque: R$"))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = saques > LIMITE_SAQUES_DIARO

        if excedeu_saldo:
            print("Operação Falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação Falhou! Valor por saque excedido.")

        elif excedeu_saques:
            print("Operação Falhou! Limites de saques diarios excedido.")
    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : R$ {valor:.2f}\n"
            print("Operação concluida com sucesso, retire as cedulas no caixa!")

        else:
            print("Valor informado invalido. Tente novamente!")

    elif opcao == "3":
        print("Operação não concluida! Serviço indisponivel")

    elif opcao == "4":
        print("\n================ EXTRATO ================")
        print("NÃO FORAM REALIZADAS NENHUMA MOVIMENTAÇÃO" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=========================================")

    elif opcao == "0":
        break

    else:
        print("Operação invalida. Favor selecione novamente a operação desejada!")



        
        


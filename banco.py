menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
excedeu_saque = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
        else:
            print("Operação falhou: O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor
        excedeu_limite = valor

        if excedeu_saldo > saldo:
            print("A operação falhou! Você não tem saldo suficiente!")

        elif excedeu_limite > limite:
            print("A operação falhou! O valor do saque excede o limite permitido!")
        
        elif excedeu_saque > LIMITE_SAQUES:
            print("A operação falhou! Número máximo de saques exedido!")
        
        elif valor <= 0:
            print("Operação falhou! O número informado é inválido!")
        
        else:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            excedeu_saque += 1
    
    elif opcao == "e":
        print("\n===============EXTRATO=============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")

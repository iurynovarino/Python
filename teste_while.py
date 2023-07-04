opcao = 1

while opcao != 0:
    opcao = int(input("[1] Sacar /n[2] Extrato /n[0] Sair /n: "))
    if opcao == 1:
        print("sacando...")
    
    elif opcao == 2:
        print("Exibindo o extrato...")
    
    elif opcao == 0:
        print("Obrigado e volte sempre!!!")
    
    else:
        print("Opção inválida!")
        
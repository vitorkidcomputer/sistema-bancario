menu = """

(1) Depositar
(2) Sacar
(3) Extrato
(4) Mostrar todos os erros possiveis
(5) Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("depósito")
        valor = float(input("informe o valor do depósito: ")) 

        if valor > 0:
             saldo += valor
             extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("erro 001=o valor informado é inválido")

    elif opcao == "2":
        print("saque")
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("erro 001=o valor informado é inválido")

        elif excedeu_limite:
            print("erro 002=o valor do saque excede o limite")

        elif excedeu_saque:
            print("erro 004=voce atingiu o limite de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1


        else:
            print("erro 005=voce nao pode sacar mais de 500 reais!💰💳💵")

    elif opcao == "3":
        print("\n++++++++++++++++++++++++++ EXTRATO ++++++++++++++++++++++++++++++++")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================================")

    elif opcao == "4":
         print("erro 005=voce nao pode sacar mais de 500 reais!💰💳💵")
         print("erro 004=voce atingiu o limite de saques")
         print("erro 003=esta operaçao é inválida")
         print("erro 002=o valor do saque excede o limite")
         print("erro 001=o valor informado é inválido")

    elif opcao == "5":
        print("parando...")
        break


    else:
        print("erro 003=esta operaçao é inválida")
        

        


   
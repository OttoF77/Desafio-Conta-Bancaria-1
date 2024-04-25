menu = """
Para extrato, digite 1
Para depositar, digite 2
Para sacar, digite 3
Para sair, digite 4
"""
saldo = 0
lim_saque = 500
QTD_SAQUE = 3
num_saque = 0
extrato = ""

while True:

    transacao = input(menu)

    if transacao == "1":

        print("\n ---------- EXTRATO ----------")
        print(f"\n Saldo Inicial: R$ {saldo: .2f}")
        print(f"\n {extrato}")
        print(f"\n Saldo Final: R$ {saldo: .2f}")
        print("\n ------------ FIM ------------")

    elif transacao == "2":

        deposito = float(input("Digite o valor do seu depósito \n"))

        if deposito <= 0:

            print("Digite o valor do depósito novamente \n")

        else:
            
            saldo = saldo + deposito
            extrato += f"Depósito: R$ {deposito: .2f} \n"

    elif transacao == "3":

        saque = float(input("Digite o valor do saque \n"))

        if saque <= 0:

            print ("Digite um valor válido \n")

        elif saque > lim_saque:

            print ("Limite de saque por operação R$ 500,00 \n")

        elif saque > saldo:

            print ("Saldo insuficiente \n")
        
        elif num_saque < QTD_SAQUE:

            saldo = saldo - saque
            extrato += f"Saque: R$ {saque: .2f} \n"
            num_saque += 1

        else:

            print ("Você já antingiu o limite diário de saques, tente novamente amanhã. \n")

    else:

        print ("Obrigado por usar nossos serviços \n")

        break
id = conta = cpf = 0   
nome = nascimento = endereco = "" 
AGENCIA = "0001" # numero da agencia
clientes = {cpf: {"id": id, "nome": nome, "nascimento": nascimento, "endereco": endereco, "conta": conta}}

# menu de opções das transações de conta corrente
def menu():

    menu_transacao = """\n
    ************* Escolha uma Transação *************
    Para extrato, digite 1
    Para depositar, digite 2
    Para sacar, digite 3
    Para nova conta, digite 4
    Para listar contas, digite 5
    Para novo usuário, digite 6
    Para sair, digite 9
    *************************************************
    """
    return input(f"{menu_transacao}")

def imprimir_extrato(saldo, extrato):

    print("---------- EXTRATO ----------\n")
    print(f"Saldo Inicial: R$ {saldo: .2f}\n")
    print(f"{extrato}\n")
    print(f"Saldo Final: R$ {saldo: .2f}\n")
    print("------------ FIM ------------\n")

def depositar(saldo, deposito, extrato,):

    if deposito <= 0:

        print("Digite o valor do depósito novamente \n")
        return

    else:
        
        saldo = saldo + deposito
        extrato += f"Depósito: R$ {deposito: .2f} \n"
    
    return saldo, extrato

def sacar(saque, LIM_SAQUE, saldo, QTD_SAQUE, extrato, num_saque):

    if saque <= 0:

        print ("Digite um valor válido \n")

    elif saque > LIM_SAQUE:

        print ("Limite de saque por operação R$ 500,00 \n")

    elif saque > saldo:

        print ("Saldo insuficiente \n")
    
    elif num_saque < QTD_SAQUE:

        saldo = saldo - saque
        extrato += f"Saque: R$ {saque: .2f} \n"
        num_saque += 1

    else:

        print ("Você já antingiu o limite diário de saques, tente novamente amanhã. \n")

    return saldo, extrato

def criar_conta(cpf, conta):

    conta += conta

    for cpf in clientes:

        return clientes.update({cpf: {conta}}), conta

def listar(cpf):

    for cpf in clientes:

        return print(f"Usuário: {clientes[cpf]['id']} \n Nome: {clientes[cpf]['nome']} \n Contas {clientes[cpf]['conta']} \n")

def criar_usuario(cpf, id, conta):

    for cpf in clientes:

        if clientes[cpf] == cpf:

            print("""Cliente já cadastrado.
                    Informe seu CPF e escolha
                    a conta corrente desejada""")
            return
            
    id += id
    
    nome = input("Digite seu nome \n")

    nascimento = input("Digite sua data de nascimento (ex: 21/05/1985) \n")

    endereco = input("Endereço: (Rua, numero - bairro - cidade/UF) \n")

    conta += conta

    return clientes.update({cpf: {"id": id, "nome": nome, "nascimento": nascimento, 
                            "endereco": endereco, "conta": conta}}), id, conta

def main():

    saldo  = 0
    extrato = ""
    LIM_SAQUE = 500
    QTD_SAQUE = 3
    num_saque = 0

    while True:

        transacao = menu()

        if transacao == "1":

            print(f"{extrato} \n")

            imprimir_extrato(saldo, extrato)

        elif transacao == "2":

            deposito = float(input("Digite o valor do seu depósito \n"))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif transacao == "3":

            saque = float(input("Digite o valor do seu saque \n"))

            saldo, extrato = sacar(saque, LIM_SAQUE, saldo, QTD_SAQUE, extrato, num_saque)

        elif transacao == "4":

            cpf = input("Digite seu CPF: \n")

            criar_conta(cpf, conta)

        elif transacao == "5":

            cpf = input("Digite seu CPF: \n")

            listar(cpf)

        elif transacao == "6":

            cpf = input("Digite seu CPF: \n")
            
            criar_usuario(cpf, id, conta)
        
        else:

            print ("Obrigado por usar nossos serviços \n")

            break
main()
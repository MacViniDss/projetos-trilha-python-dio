

def Menu(): 
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar usuário
    [5] Criar conta
    [6] Ver contas
    [7] Sair
    => """
    return input(menu)

def Deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        
        print(f"\nDeposito realizado de R${valor}")
   
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def Extrato(extrato, /, *, saldo):
        print("\n================ EXTRATO ================")
        
        print("Não foram realizadas movimentações." if not extrato else extrato)
        
        print(f"\nSaldo: R$ {saldo:.2f}")
        
        print("==========================================")

def Saque(*, saldo, valor, extrato, limite_valor, numero_saques, limite_saques):
    if valor > saldo:
        print("\nSaldo insuficiente")
    
    elif valor > limite_valor:
        print("\nSaque acima do limite")

    elif numero_saques >= limite_saques:
        print("\nLimite de saque diario excedido")

    elif valor > 0:
        saldo -= valor
        extrato += (f"Saque: R$ {valor:.2f}\n")
        numero_saques = numero_saques + 1
        
        print(f"\nSaque realizado de R$ {valor}")
        print(f"\nSaque realizado {numero_saques}")

    else:
        print("\nValor de saque invalido")
    
    return saldo, extrato, numero_saques

def Criar_user(clientes):
    cpf = int(input("Digite seu cpf: "))
    for c in clientes:
        if c["cpf"] == cpf:
            print("Ususario ja existe")
            return
                           
    print("\nVamos criar seu usario:")

    nome = input("Escreva seu nome ")
    data_nasc = input("Me diga sua data de nascimento ")
    endereço = input("Me informe o estado em que reside ")

    user = {
        "cpf": cpf,
        "nome": nome,
        "data_nasc": data_nasc,
        "endereço" : endereço
    }
    clientes.append(user)
    print("\nUsuario criado com sucesso")

def Criar_conta(agencia, n_conta, clientes):
    cpf = int(input("Digite seu cpf: "))

    for c in clientes:
        if c["cpf"] == cpf:
            print("\nUsusario no sistema")
            print("\nConta criada!")
            return {"agencia": agencia, "n_conta": n_conta, "usuario": cpf}
    
    print("Ususario não existe")


def App():
    saldo = 0
    limite = 500
    extrato = ""
    agencia = "0001"
    numero_saques = 0
    LIMITE_SAQUES = 3

    contas = []
    clientes = []

    while True:

        opcao = Menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = Deposito(saldo, valor, extrato)

        elif opcao == "3":
            Extrato(extrato, saldo=saldo)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = Saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite_valor=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

        elif opcao == "4":
            print("Criação de usuario:")
            Criar_user(clientes)

        elif opcao == "5":
            n_conta = len(contas) + 1
            conta = Criar_conta(agencia, n_conta, clientes)    
            if conta:
                contas.append(conta)

        elif opcao == "6":
            print("Aqui estão as contas cadastradas: ")
            print(contas)


        elif opcao == "7":
            print("OPERAÇÃO FINALIZADA!!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


App()

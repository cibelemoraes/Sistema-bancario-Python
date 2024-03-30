import textwrap

def menu():
    menu = """\n
    ============== MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n===Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido.@@@" )
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operção falhou! Você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operção falhou! O valor do sauqe excedeu o limite. @@@")
        
    elif excedeu_saques:
        print("\n@@@ Operção falhou! Número máximo de saques excedido. @@@")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\t R$ {valor:. 2f}\n"
        numero_saques += 1
        print("\n====== Saque realizadp com sucesso! ====")
        
    else: print("\n@@@ Operção falhou! O valor informado é invalido. @@@")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
   print("\n============== EXTRATO =============")
   print("Não foram realizadas movimentações." if not extrato else extrato)
   print(f"\nSaldo:\t\tR$ {saldo:.2f}")
   print("======================================")
   
def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuarios = filtrar_usuario(cpf, usuarios)
    
    if usuarios:
        print("\n @@@ Já exite  usuario com esse CPF! @@@")
        return
    nome = input("Informe o nome completo")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, n, bairro, cidade/ estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("========Usuario criado com sucesso!=========")
        
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None    
    
    
def  criar_conta(agencia, numero_conta, usuarios):
    
    
def listar_contas(contas):
    
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "00001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True
        opcao = menu()
        
        if opcao =="d":
            
        elif opcao =="s":
            
        elif opcao =="e":
            
        elif opcao =="nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas)
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao =="q":
            break
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada. ")
        
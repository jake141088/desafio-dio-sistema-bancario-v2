# Função para exibir o menu e obter a opção do usuário
def exibir_menu():
    return input("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """)

# Função para realizar um depósito
def realizar_deposito():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar um saque
def realizar_saque():
    global saldo, extrato, numero_saques
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1

# Função para exibir o extrato
def exibir_extrato():
    global saldo, extrato
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Variáveis globais
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa
while True:
    opcao = exibir_menu()
    if opcao == "d":
        realizar_deposito()
    elif opcao == "s":
        realizar_saque()
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

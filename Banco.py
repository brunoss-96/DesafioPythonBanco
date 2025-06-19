from datetime import datetime

LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

saldo = 0
extrato = ""
numero_saques = 0
cliente = ""

def mostrar_menu():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
    return f"""
Olá {cliente}, Bem Vindo ao SantoAndre Bank !
Saldo Atual: R$ {saldo:.2f}  Data/Hora: {agora}


Escolha uma das opções abaixo:

[d] Depositar
[s] Sacar
[ex] Extrato analítico
[q] Sair

=> """

def deposito(valor):
    global saldo, extrato
    if valor <= 0:
        print("Valor inválido para depósito.")
        return
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def saque(valor):
    global saldo, extrato, numero_saques
    if valor <= 0:
        print("Valor inválido para saque.")
        return
    if valor > saldo:
        print("Saldo insuficiente.")
        return
    if valor > LIMITE_VALOR_SAQUE:
        print("Saque excede o limite permitido.")
        return
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diário atingido.")
        return
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def mostrar_extrato():
    print("------- Extrato --------")
    print()
    print(extrato.strip() if extrato else "Nenhuma movimentação.")
    print()
    print(f"Saldo atual: R$ {saldo:.2f}")
    print()
    print("-------------------------")

def main():
    global cliente
    cliente = input("Olá! Digite seu nome: ").strip()

    while True:
        opcao = input(mostrar_menu()).strip().lower()
        
        if opcao == "d":
            try:
                valor = float(input("Valor do depósito: R$ "))
                deposito(valor)
            except ValueError:
                print("Entrada inválida. Use números.")
        
        elif opcao == "s":
            try:
                valor = float(input("Valor do saque: R$ "))
                saque(valor)
            except ValueError:
                print("Entrada inválida. Use números.")

        elif opcao == "ex":
            mostrar_extrato()

        elif opcao == "q":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

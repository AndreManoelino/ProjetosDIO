menu = """

[1] Deppositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$"))

        if valor  > 0:
            saldo += valor
            extrato += f'Depósito; R$ (valor:.2f)\n'

        else:
            print("Operação falhou! O valor informado é inválido .")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$")) 
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        execedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("OPeração falhou! Você nao tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou ! O valor do saque excede o limite.")    
                
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print('Bem vindo a sua conta!')

operacao = -1

while operacao != 0:
    print('\nO que deseja fazer agora?')
    operacao = int(input('[1] Depositar \n[2] Sacar \n[3] Extrato \n[0] Finalizar\n:'))
    
    if operacao == 1:
        deposito = float(input('Qual valor deseja depositar?\n'))
        if deposito < 0:
            print('Operação falhou. O valor informado é inválido.')
        else:
            saldo += deposito
            extrato += (f"Depósito: R$ {deposito:.2f}\n")
            print(' ')
            print('**Depósito realizado com sucesso!**')

    elif operacao == 2:
        saque = float(input('Qual valor deseja sacar?\n'))
        
        if saque < 0:
            print('Operação falhou. O valor informado é inválido.')
        else:
            if saque > saldo:
                print('Saldo insuficiente.\n ')
            elif saque > limite:
                print('Operação falhou! O valor do saque excede o limite por operação.')
            elif numero_saques >= LIMITE_SAQUES:
                print('Operação falhou! Número máximo de saques excedido.')
            else:
                saldo -= saque
                numero_saques += 1
                extrato += (f"Saque: R$ {saque:.2f}\n")
                print('Saque realizado com sucesso!')

    elif operacao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    else:
        print("\nObrigado por usar nosso sistema bancário. Até logo!")


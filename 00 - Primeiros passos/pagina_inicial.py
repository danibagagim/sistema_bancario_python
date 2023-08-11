operacao = -1

while operacao != 0:
    operacao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n:'))

    if operacao == 1:
        print('Sacando...')
    elif operacao == 2:
        print('Exibindo extrato...')
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

# input("Selecione a operação desejada:")
# print("1 - Extrato Conta Corrente")
# print("2 - Extrato Conta Poupança")
# print("3 - Saque")


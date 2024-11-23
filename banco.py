menu = """
##########-MENU-##########
   [1]-Deposito
   [2]-Saque
   [3]-Extrato
   [4]-Sair
##########################
"""

conta_cliente = 0
contador_saquediario = 0
extrato = ""

while True:
    print(menu)
    opcao = int(input("Insira a Opção: "))

    if opcao == 1:
        deposito = float(input("Insira o valor que deseja depositar: "))
        conta_cliente += deposito
        extrato += f"foi depositado: {deposito:.2f}\n"


    elif opcao == 2:

        if contador_saquediario<3:
            sacar = float(input("quanto deseja sacar?"))
            if sacar <= 500:
                if sacar <= conta_cliente:
                    conta_cliente -= sacar
                    contador_saquediario += 1
                    extrato += f"foi sacado: R${sacar:.2f}\n"
                else: 
                    print("Voce nao possui saldo suficiente!")
            else:
                print("Seu saque deve ser menor que R$500,00!")
        else:
            print("Voce atingiu o limite de Saques Diarios!")

        continue
    elif opcao == 3:

        if extrato == "":
            extrato = "Nao foram realizadas movimentacoes"

        print("------EXTRATO--------")
        print(extrato)
        print(f"Voce possui R${conta_cliente:.2f}")
        print("---------------------")

    elif opcao == 4:
        break

    else:
        print("Selecione uma opcao correta!")


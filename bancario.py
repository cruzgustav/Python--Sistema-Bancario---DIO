## função depositar:
saldo = 0                        ## Saldo
extrato = []                     ## Historico de transações
total_Depositado = 0             ## Valor total depositado
total_Sacado = 0                 ## Valor total sacado 
limite_Saque = 1500              ## Valor limite de saques
limite_Saque_Diario = 500        ## Valor limite por cada saque
quantidade_Saque = 0             ## Armazenar quantos saques o cliente fez 
limite_Quantidade_Saque = 3      ## Limite de quantidade de saques diarios 

def depositar(valor):           ## Função de Deposito
    global saldo, extrato, total_Depositado, total_Sacado, limite_Saque, limite_Saque_Diario, limite_Quantidade_Saque, quantidade_Saque
    if valor > 0:
        saldo = saldo + valor
        print(F"{valor} depositados com sucesso!")
        total_Depositado = total_Depositado + valor
        extrato.append(f'Você depositou R${valor:.2f}, seu saldo atual é de R${saldo:.2f}')
    else :
        print('Valor inválido, tente novamente!')
def historico():                ## Função de Historico / Extrato
    global extrato
    print('Histórico de transações:')
    for item in extrato:
        print(item)
    print(f'Total depositado: R${total_Depositado:.2f}')
    print(f'Total sacado: R${total_Sacado:.2f}')
def sacar(valor):               ## Função de Saque
    global saldo, extrato, total_Depositado, total_Sacado, limite_Saque, limite_Saque_Diario, limite_Quantidade_Saque, quantidade_Saque
    if valor <= limite_Saque_Diario and valor <= saldo and limite_Saque_Diario <= limite_Saque: ## Regras de saque
        saldo = saldo - valor                                                                   ## Operação se saque
        print(F"{valor} sacados com sucesso!")
        total_Sacado = total_Sacado + valor                                                     ## Armazenar e Somar ao Total sacado                                                   
        quantidade_Saque = quantidade_Saque + 1                                                 ## Contar / adicionar na quandidade de saques 
        extrato.append(f'Você sacou R${valor:.2f}, seu saldo atual é de R${saldo:.2f}')
while True:                     ## Loop para repetição do menu
    print(f'''                  
    Bem-vindo ao Banco XYZ!

        SALDO: {saldo} 
        
    Escolha uma das opções abaixo para continuar:
      1 - Depositar
      2 - Extrato
      3 - Sacar
      4 - Sair
      ''')
    x = int(input("#####: "))
    if x == 1:                 ## Depositar 
        valor = int(input('Digite o valor a ser depositado: '))
        if valor <= 0:
            print('Valor inválido, tente novamente!')
        depositar(valor)
    elif x == 2:               ## Historico
        historico()
    elif x == 3:               ## Saque 
        valor = float(input('Digite o valor a ser sacado: '))
        if valor <= 0 : 
            print("Valor invalido!")
        elif quantidade_Saque >2:
            print("Você atingiu o limite de saques diários!") 
        elif valor > saldo:
            print("Saldo insuficiente!")
        elif valor >= limite_Saque:
            print("Você atingiu o valor limite de saque diário!")
        else:
            sacar(valor)
    elif x == 4:               ## Saldo
        print("Até logo!")
        break
    else:
        print('Opção inválida, tente novamente!')
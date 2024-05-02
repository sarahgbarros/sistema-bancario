menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


"""

saldo = 1200
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True :
    
    opcao = input(menu)
    
    if opcao == "d":
       print(f"SAlDO ATUAL: R${saldo} ")
       valor = float(input("Informe o valor do depósito:"))
       if valor > 0 :
          saldo += valor
          extrato += f"Depósito: R${valor:.2f}\n" 
       else :
           print("Operação falhou: O valor informado é invalido")  

    elif opcao == "s":
       print(f"SAlDO ATUAL:{saldo} ")
       valor = float(input("Informe o valor do saque:"))
       
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saque = numero_saque > LIMITE_SAQUE

       if excedeu_saldo:
           print("Operação falhou: Saldo insuficiente")
         
       elif excedeu_limite :
           print("Operação falhou: limite de saque insuficiente")
       
       elif excedeu_saque:
           print("Operação falhou: quantidade de saque excedida")
        
       elif valor > 0 :
           saldo -= valor
           extrato += f"Saque: R${valor:.2f}\n"
           numero_saque += 1
       else :
           print("Operação falhou : O valor informado é invalido") 

    elif opcao == "e":
       print("\n################## EXTRATO ##################")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\n Saldo: R$ {saldo:.2f}")
       print("#############################################")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operacao desejada")


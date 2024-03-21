from tkinter import Menu


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numeros_saques = 3

while True:
     opcao = input(Menu)

     if opcao == "d":
          valor = float(input("informe o valor depositado: "))
    
        if valor > 0:
          saldo += valor
          extrato += f"Depósito : R$ {valor:.2f}\n"
        
        else:
          print("Operação falho! O valor informado é invalido.")

     elif opcao == "s":
         
         valor = float(input("informe o valor do saque: "))
     
         excedeu_saldo = valor > saldo

         excedeu_limite = valor > limite
 
         excedeu_saques = numeros_saques

     if excedeu_saldo:
         print("Operação falhou! você não possui saldo suficiente.")

     elif excedeu_limite:
         print("Operação falhou! O valor do saque excedeu o limite.")

     elif excedeu_saques:
         print("Operação falhou! numero maximo de saques excedido. ")

     else:
         print("Operação falhou! O valor informado é inválido. ")
  
    elif opcao == "e": 
        print("\n ========== Extrato =======")     
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$"{saldo:.2f})
        print("===============================")

    elif opcao == "q"
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")      






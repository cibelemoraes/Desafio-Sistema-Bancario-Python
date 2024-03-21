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
        valor = float(input("Informe o valor do saque"))
    
    execedeu_saldo = valor > saldo
    execedeu_saldo = valor > saldo
    execedeu_saldo = valor > saldo

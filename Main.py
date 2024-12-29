from cliente import cliente
from Conta import Conta

print("Bem-vindo ao sistema bancário!")

# Coletando informações do usuário para criar o cliente
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")

# Criando o cliente e a conta
c1 = cliente(nome, telefone)
conta = Conta(c1.get_nome(), 1222)

print(f"Conta criada com sucesso para {c1.get_nome()}!")

# Menu interativo para realizar operações
while True:
    print("\nEscolha uma operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver extrato")
    print("4. Sair")
    opcao = input("Digite a opção desejada (1-4): ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        conta.deposita(valor)
        print("Depósito realizado com sucesso!")
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        conta.saque(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        print("Saindo... Obrigado por usar o sistema!")
        break
    else:
        print("Opção inválida. Tente novamente.")

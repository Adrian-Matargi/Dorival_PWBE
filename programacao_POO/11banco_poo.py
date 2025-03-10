class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        return f"Cliente(nome={self.nome}, cpf={self.cpf})"


class ContaBancaria:
    def __init__(self, cliente, numero_conta, saldo_inicial=0.0):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return False
        self.saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
        return True

    def deposito(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo!")
            return False
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
        return True

    def transferencia(self, outra_conta, valor):
        if self.saque(valor):
            outra_conta.deposito(valor)
            print(f"Transferência de R${valor} realizada com sucesso para a conta {outra_conta.numero_conta}.")
            return True
        return False

    def __repr__(self):
        return f"ContaBancaria(cliente={self.cliente.nome}, numero_conta={self.numero_conta}, saldo={self.saldo:.2f})"


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente

    def abrir_conta(self):
        cliente = self.buscar_cliente()
        if cliente:
            numero_conta = int(input("Digite o número da nova conta: "))
            saldo_inicial = float(input("Digite o saldo inicial da conta: "))
            conta = ContaBancaria(cliente, numero_conta, saldo_inicial)
            self.contas.append(conta)
            print(f"Conta {numero_conta} aberta com sucesso para {cliente.nome}!")
            return conta
        else:
            print("Cliente não encontrado!")
            return None

    def buscar_cliente(self):
        cpf = input("Digite o CPF do cliente para buscar: ")
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        print("Cliente não encontrado!")
        return None

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print("Conta não encontrada!")
        return None

    def realizar_operacao(self):
        print("\nEscolha a operação desejada:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Transferência")
        print("4 - Sair")
        escolha = input("Digite o número da operação: ")

        if escolha == "1":
            conta = self.buscar_conta(int(input("Digite o número da conta: ")))
            if conta:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.deposito(valor)
        elif escolha == "2":
            conta = self.buscar_conta(int(input("Digite o número da conta: ")))
            if conta:
                valor = float(input("Digite o valor a ser sacado: "))
                conta.saque(valor)
        elif escolha == "3":
            conta_origem = self.buscar_conta(int(input("Digite o número da conta de origem: ")))
            if conta_origem:
                conta_destino = self.buscar_conta(int(input("Digite o número da conta destino: ")))
                if conta_destino:
                    valor = float(input("Digite o valor a ser transferido: "))
                    conta_origem.transferencia(conta_destino, valor)
        elif escolha == "4":
            print("Saindo...")
            return False
        else:
            print("Opção inválida. Tente novamente.")
        return True


# Exemplo de uso:
banco = Banco("Banco Exemplo")

while True:
    print("\nMenu do Banco:")
    print("1 - Cadastrar cliente")
    print("2 - Abrir conta")
    print("3 - Realizar operação")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        banco.cadastrar_cliente()
    elif opcao == "2":
        banco.abrir_conta()
    elif opcao == "3":
        if not banco.realizar_operacao():
            break
    elif opcao == "4":
        print("Saindo do banco.")
        break
    else:
        print("Opção inválida. Tente novamente.")

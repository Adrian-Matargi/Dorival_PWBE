class ContaBancaria:
    def __init__(self, num_conta, nome_titular, saldo):
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
    
    def saque(self):
        valor_saque = float(input("Quanto você quer sacar?: "))
        return self.saldo - valor_saque

    def depósitos(self):
        valor_deposito = float(input("Quanto você quer depositar?: "))
        return self.saldo + valor_deposito
    
    def __str__(self):
        return f"Bem vindo a conta {self.num_conta} do titular {self.nome_titular}. Seu saldo é de: {self.saldo}"

conta = ContaBancaria(1234, "Adrian", 5000)

print(conta)
decisao = int(input("Sacar(1) - Depositar(2) - Sair(3) - Qual opção você deseja?: "))

if decisao == 1 :
    print(conta.saque())
elif decisao == 2 :
    print(conta.depósitos())
else:
    print("Obrigado!")
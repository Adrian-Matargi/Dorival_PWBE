class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar(self):
        nome = input("Digite o nome do contato: ")
        numero = int(input("Digite o número de telefone: "))
        contato = Agenda(nome, numero)
        self.contatos.append(contato)
    
    def editar(self):
        
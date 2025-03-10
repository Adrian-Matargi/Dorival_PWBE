class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def adicionar_consulta(self):
        consulta = input("Digite o motivo da consulta: ")
        self.historico_consultas.append(consulta)
        print("Consulta adicionada com sucesso!")
    
    def exibir_consultas(self):
        if not self.historico_consultas:
            print("O paciente não possui consultas registradas.")
        else:
            print(f"Histórico de consultas de {self.nome}:")
            for consulta in enumerate(self.historico_consultas, 1):
                print(consulta)


paciente = Paciente("João Silva", 35)
print(f"Paciente: {paciente.nome}, Idade: {paciente.idade} anos")

decisao = 0
while decisao != 3:
    decisao = int(input("(1)-Adicionar consulta (2)-Exibir histórico de consultas (3)-Sair: "))

    if decisao == 1:
        paciente.adicionar_consulta()
    
    elif decisao == 2:
        paciente.exibir_consultas()
    
    elif decisao == 3:
        print("Até logo!")

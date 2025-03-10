class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.nota = notas
    
    def media(self):
        return sum(self.nota) / len(self.nota)
    
    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

aluno = Aluno("Adrian", 1234, [10, 9, 10, 8, 10])

print(f"O Aluno {aluno.nome} de matrícula {aluno.matricula} possuí média {aluno.media()}")
print(f"Aluno {aluno.situacao()}")
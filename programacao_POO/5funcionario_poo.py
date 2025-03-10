class Funcionario:
    def __init__(self, nome, salario, cargo, impostos, beneficios):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.impostos = impostos
        self.beneficios = beneficios
    
    def salario_liquido(self):
        desconto_impostos = (self.impostos / 100) * self.salario
        salario_liquido = self.salario - desconto_impostos + self.beneficios
        return salario_liquido
    

funcionario = Funcionario("Adrian", 5000, "Analista", 15, 800)

print(f"Funcionário {funcionario.nome}, Cargo de {funcionario.cargo}")
print(f"Salário Bruto: R${funcionario.salario}")
print(f"Com impostos de {funcionario.impostos}% e beneficios de R${funcionario.beneficios}")
print(f"Salário Líquido é de: R${funcionario.salario_liquido()}")
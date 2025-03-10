class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        aumentar_velo = int(input("Quantos km/h você quer atingir?: "))
        self.velocidade = aumentar_velo + self.velocidade
        return f"A velocidade atual é {self.velocidade} Km/h"
    
    def frear(self):
        escolha = int(input("Você deseja diminuir a velocidade ou parar o carro? (1) - Diminuir (2) - Parar"))

        if escolha == 1:
            self.velocidade = self.velocidade / 2
            return f"A velocidade atual é {self.velocidade} Km/h"
        
        elif self.velocidade == 0:
            print("O carro já está parado!")

        else:
            self.velocidade = 0
            return f"A velocidade atual é {self.velocidade} Km/h"

carro = Carro("Porshce", "GT3 RS", 0)
print(f"O carro é um(a) {carro.modelo} da maraca {carro.marca} e ele está {carro.velocidade} Km/h")
decisao = 0

while decisao != 3:
    decisao = int(input("(1)-Acelerar (2)-Frear (3)-Sair do carro"))

    if decisao == 1:
        print(carro.acelerar())
    
    elif decisao == 2:
        print(carro.frear())
    
    elif decisao == 3:
        print("Até logo!")
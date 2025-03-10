class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
circulo = Retangulo(10, 5)
print(f"Área: {circulo.area()}")
print(f"Perímetro: {circulo.perimetro()}")
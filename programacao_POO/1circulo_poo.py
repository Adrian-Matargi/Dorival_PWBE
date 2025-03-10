class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raio
    
circulo = Circulo(5)
print(f"Área: {circulo.area()}")
print(f"Perímetro: {circulo.perimetro()}")
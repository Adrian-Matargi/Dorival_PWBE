import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def valido(self):
        return (self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1)

    def area(self):
        if not self.valido():
            return "Não é um triângulo válido"
    
        semiperimetro = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(semiperimetro * (semiperimetro - self.lado1) * (semiperimetro - self.lado2) * (semiperimetro - self.lado3))
        return area
    
triangulo = Triangulo(3, 4, 5)

if triangulo.valido():
    print(f"Área do Triângulo: {triangulo.area():.2f}")
else:
    print("Os lados não formam um triângulo válido.")
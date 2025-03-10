class Cachorro:
    def __init__(self, nome, raca, cor, idade):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.orelhas = 2
    
    def latir(self):
        print(f"{self.nome} diz: au au")
    
    def correr(self, kms):
        print(f"{self.nome} correu {kms} km")


class Livro:
    def __init__(self, categoria, titulo, autor, personagens, indicadores):
        self.genero = categoria
        self.titulozinho = titulo
        self.escritor = autor
        self.indicacao = indicadores
        self.personagens = personagens
    def abrir(self, pagina):
        print(f"O livro {self.titulozinho} foi aberto na pagina {pagina}")

    def __str__(self):
        return f"{self.titulozinho} do genero {self.genero} escrito por {self.escritor}"
    
    def __eq__(self, value):
        if (isinstance(value, Livro)):
            titulo_igual = self.titulozinho == value.titulozinho
            autores_iguais = self.escritor == value.escritor
            return titulo_igual and autores_iguais
        else:
            return False

livro_da_kamila = Livro("Romance", "Crepusculo", "J.K Rowlling", ["Bela", "Edward"], 14)
livro_da_kamila.abrir(10)

print(livro_da_kamila)
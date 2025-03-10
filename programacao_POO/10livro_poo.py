class Livro:
    def __init__(self, titulo, autor, numero_pag):
        self.titulo = titulo
        self.autor = autor
        self.numero_pag = numero_pag

    def emprestar(self):
        if self in livros_disponiveis:
            livros_disponiveis.remove(self)
            livros_emprestados.append(self)
            print(f'Livro "{self.titulo}" emprestado!')
        else:
            print(f'O livro "{self.titulo}" não está disponível no momento.')

    def devolver(self):
        if self in livros_emprestados:
            livros_emprestados.remove(self)
            livros_disponiveis.append(self)
            print(f'Livro "{self.titulo}" devolvido!')
        else:
            print(f'O livro "{self.titulo}" não estava emprestado.')

    def consultar(self):
        return f'Livros disponíveis: {[livro.titulo for livro in livros_disponiveis]}'


# Criando os livros
livro1 = Livro("Crepúsculo", "Stephenie Meyer", 384)
livro2 = Livro("Harry Potter", "J.K. Rowling", 208)
livro3 = Livro("1984", "George Orwell", 328)

# Listas de livros disponíveis e emprestados
livros_emprestados = []
livros_disponiveis = [livro1, livro2, livro3]

def exibir_estado():
    print(f"\nLivros disponíveis: {[livro.titulo for livro in livros_disponiveis]}")
    print(f"Livros emprestados: {[livro.titulo for livro in livros_emprestados]}\n")

while True:
    print("Bem-vindo ao sistema de empréstimo de livros!")
    print("1. Pegar livro emprestado")
    print("2. Devolver livro")
    print("3. Consultar livros disponíveis")
    print("4. Sair")
    
    decisao = int(input("Escolha uma opção (1, 2, 3, ou 4): "))

    if decisao == 1:
        escolha = int(input("Qual livro você quer pegar emprestado? (1)-Crepúsculo (2)-Harry Potter (3)-1984: "))
        if escolha == 1:
            livro1.emprestar()
        elif escolha == 2:
            livro2.emprestar()
        elif escolha == 3:
            livro3.emprestar()
        
    elif decisao == 2:
        escolha = int(input("Qual livro você quer devolver? (1)-Crepúsculo (2)-Harry Potter (3)-1984: "))
        if escolha == 1:
            livro1.devolver()
        elif escolha == 2:
            livro2.devolver()
        elif escolha == 3:
            livro3.devolver()

    elif decisao == 3:
        print(livro1.consultar())

    elif decisao == 4:
        print("Saindo do sistema...")
        break

    exibir_estado()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto(nome={self.nome}, Preço={self.preco})"


class LojaVirtual:
    def __init__(self):
        self.produtos = []
        self.carrinhos = []

    def cadastrar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$"))
        produto = Produto(nome, preco)
        self.produtos.append(produto)  # Agora adiciona o produto à lista
        print(f"Produto {nome} cadastrado com sucesso!")

    def listar_produtos(self):
        if not self.produtos:
            print("Não há produtos cadastrados.")
            return
        print("\nProdutos disponíveis na loja:")
        for produto in self.produtos:
            print(produto)

    def criar_carrinho(self):
        carrinho = Carrinho()
        self.carrinhos.append(carrinho)
        return carrinho

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():  # Busca sem diferenciar maiúsculas de minúsculas
                return produto
        print(f"Produto {nome} não encontrado!")
        return None


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade=1):
        self.itens.append({"produto": produto, "quantidade": quantidade})

    def calcular_total(self):
        total = sum(item["produto"].preco * item["quantidade"] for item in self.itens)
        return total

    def __repr__(self):
        if not self.itens:
            return "O carrinho está vazio."
        return '\n'.join([f"{item['produto'].nome} x{item['quantidade']} - R${item['produto'].preco * item['quantidade']:.2f}" for item in self.itens])


# Função principal para interação
def main():
    loja = LojaVirtual()
    
    while True:
        print("\nMenu da Loja Virtual:")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Criar carrinho de compras")
        print("4 - Adicionar produto ao carrinho")
        print("5 - Calcular total do carrinho")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.cadastrar_produto()
        elif opcao == "2":
            loja.listar_produtos()
        elif opcao == "3":
            carrinho = loja.criar_carrinho()
            print("Carrinho de compras criado com sucesso!")
        elif opcao == "4":
            nome_produto = input("Digite o nome do produto a ser adicionado: ")
            produto = loja.buscar_produto(nome_produto)
            if produto:
                quantidade = int(input("Digite a quantidade do produto: "))
                carrinho.adicionar_produto(produto, quantidade)
                print(f"{quantidade} unidades de {produto.nome} adicionadas ao carrinho.")
        elif opcao == "5":
            print("\nItens no Carrinho:")
            print(carrinho)
            print(f"\nTotal do carrinho: R${carrinho.calcular_total():.2f}")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

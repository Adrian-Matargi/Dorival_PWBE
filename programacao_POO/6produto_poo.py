class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_estoque(self):
        valor_stoq = self.preco * self.quantidade
        return valor_stoq
    
    def verificacao(self):
        if self.quantidade > 0:
            print("Produto disponível!")
        else :
            print("Produto indisponível!")

produto = Produto("Banana", 5, 20)

print(f"O produto {produto.nome} com preço unitário de R$ {produto.preco} e quantidade em estoque de {produto.quantidade}")
print(f"O valor total do esoque é de {produto.valor_estoque()}")
print(produto.verificacao())
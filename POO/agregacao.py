class Carrinho:
    def __init__(self):
        self.produtos = []

    def total(self):
        return sum(p.preco for p in self.produtos)
    
    def inserir_produto(self,*produto):
        for p in produto:
            print('ok')
            self.produtos.append(p)

    def listar_produto(self):
        print("Lista de produtos")
        for p in self.produtos:
            print(f'Nome: {p.nome} Preço: {p.preco}')

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1, p2 = Produto("Chocolate", 10), Produto("Pão", 20)

carrinho = Carrinho()
print(carrinho.inserir_produto(p1,p2))
carrinho.listar_produto()

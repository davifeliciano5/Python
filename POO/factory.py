class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def idade_50(cls,nome):
        return cls(nome,50)
    
    @classmethod
    def anonimo(cls,idade):
        return cls('anonimo', idade)

p1 = Pessoa.anonimo(30)
p2 = Pessoa.idade_50("Davi")
print(p1.nome, p1.idade)
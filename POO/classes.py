class pessoa:

    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class carro:
    def __init__(self,nome='BMW'):
        self.nome = nome

    def acelerar(self):
        print(f'O carro {self.nome} está acelerando!')

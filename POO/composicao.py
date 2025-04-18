class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append(Endereco(rua,numero))

    def inserir_endereco_externo(self,endereco):
        self.endereco.append(endereco)

    def listar_enderecos(self):
        for e in self.endereco:
            print(f"Rua: {e.rua} Número: {e.numero}")

    def __del__(self):
        print(f'Apagado {self.nome} o cliente')

class Endereco:
    def __init__(self,rua ,numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'O endereço foi apagado {self.rua} {self.numero}')


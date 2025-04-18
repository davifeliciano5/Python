import json

class Pessoa:
    ano_atual = 2025

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome':'Davi Feliciano', 'idade':20}
primeiro = Pessoa(**dados)
print(primeiro.nome)
print(primeiro.get_ano_nascimento())
print(vars(primeiro))

dados2 = vars(primeiro)
print(dados2)
with open('arquivo.json','w') as a:
    json.dump(dados2,a)
   
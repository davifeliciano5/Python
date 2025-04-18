import json
caminho = "arquivo.json"

class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Davi","Feliciano")
p2 = Pessoa("Carlos","Oliveira")

bd = [vars(p1),vars(p2)]

with open(caminho,'w') as a:
    print("Fazendo DUMP")
    json.dump(bd,a)

if __name__ == "__main__":
    # Só será executado se rodar diretamente o gravar.py
    dados = {'nome': 'Davi', 'idade': 20}
    with open(caminho, 'w') as a:
        json.dump([dados], a)
    print("Arquivo JSON criado!")
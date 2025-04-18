"""
Em Python, tudo que está no nível superior de um arquivo
 (fora de funções ou classes) 
é executado automaticamente quando o arquivo é importado.
"""

import json
from gravar import caminho,Pessoa

with open(caminho,'r') as a:
    dados = json.load(a)

    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])

    print(p1.nome)
    print(p2.nome)
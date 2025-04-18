class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,valor):
        self._ferramenta = valor

class FerramentaEscrever:
    
    def __init__(self,nome):
        self.nome = nome
    
    def escrever(self):
        return f'A feramenta {self.nome} está escrevendo'
    

e1 = Escritor("Davi")
caneta = FerramentaEscrever("Canetão")
e1.ferramenta = caneta
print(e1.ferramenta.escrever())
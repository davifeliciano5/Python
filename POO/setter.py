class Caneta:

    def __init__(self,cor,cor_tampa):
        self.cor = cor
        self._cor_tampa = cor_tampa

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self,valor):
        self.cor_tampa = valor

    @property
    def cor(self):
        print("Estou no getter")
        return self._cor
    
    @cor.setter
    def cor(self,valor):
         print("Estou no setter")
         self._cor = valor
    
c1 = Caneta("preta","rosa")
print(c1.cor)
c1.cor = "azul"
print(c1.cor)
print(c1.cor_tampa)
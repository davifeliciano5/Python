class Caneta:
    
    def __init__(self,cor_tinta):
        self.cor_tinta = cor_tinta

    @property
    def cor(self):
        return self.cor_tinta

c1 = Caneta("Amarelo")
print(c1.cor)
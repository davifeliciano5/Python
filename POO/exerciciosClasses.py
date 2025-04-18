class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.fabricante = None
        self.motor = None

    def inserir_fabricante(self,fabricante):
        self.fabricante = Fabricante(fabricante)
    
    def inserir_motor(self,motor1):
        self.motor = Motor(motor1)


class Motor:
    def __init__(self,nome):
        self.nome = nome

class Fabricante:
    def __init__(self,nome):
        self.nome = nome

celta = Carro('Celta')
celta.inserir_fabricante("GM")
celta.inserir_motor("VHC")

print(celta.fabricante.nome)
print(celta.nome)
print(celta.motor.nome)
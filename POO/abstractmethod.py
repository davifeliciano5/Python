#from abc import ABC

class a():

    def __init__(self, name):
        self._name = None
        self.name = name
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, nome):
        self._name = nome

p1 = a('Davi')
print(p1.name)
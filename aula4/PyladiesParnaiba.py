from abc import ABC, abstractmethod

class PyladiesParnaiba:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def pasta(self):
        pass

    @abstractmethod
    def funçao(self):
        pass
    
    def imprimir(self):
       print(f'A membra {self.nome} perticipa da pasta {self.pasta()} responsável por {self.funçao()}') 
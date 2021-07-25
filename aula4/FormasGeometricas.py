from abc import ABC, abstractmethod

class FormasGeometricas:
    def __init__(self, *lados):
        self.lados = lados

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def imprimi(self):
        print(f'Area: {self.area()}m² | Perímetro: {self.perimetro()}m')

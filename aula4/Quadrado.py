import FormasGeometricas as forms

class Quadrado(forms.FormasGeometricas):
    def __init__(self, *lados):
        super().__init__(*lados)

    def area(self):
        return self.lados[0] ** 2

    def perimetro(self):
        return self.lados[0] * 4

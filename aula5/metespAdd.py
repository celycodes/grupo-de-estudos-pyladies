class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, outrafracao):
        denominador = self.denominador * outrafracao.denominador
        numerador = self.numerador * outrafracao.denominador + outrafracao.numerador * self.denominador
        return Fracao(numerador,denominador)

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

umTerco = Fracao(1,3)
umQuinto = Fracao(1,5)
print(umTerco + umQuinto)

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 5 - Herança Multipla + Metodos especiais
* metodo especial __add__ na prática
'''
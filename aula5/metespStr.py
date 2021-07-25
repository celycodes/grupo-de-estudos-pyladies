class Pylady:
    def __init__(self, nome, membras):
        self.nome = nome
        self.membras = membras

    def __str__(self):
        return f'Capítulo: {self.nome}\nMembras: {self.membras}'

pyladiesphb = Pylady('PyLadies Parnaíba',['Celenny','Emilly','Vitória','Karina','Alinne','Ana'])
print(pyladiesphb)

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 5 - Herança Multipla + Metodos especiais
* metodo especial __str__ na prática
'''
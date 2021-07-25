class Pylady:
    def __init__(self, nome, membras):
        self.nome = nome
        self.membras = membras

    def __getitem__(self, item):
        return self.membras[item]

pyladiesphb = Pylady('PyLadies Parnaíba',['Celenny','Emilly','Vitória','Karina','Alinne','Ana'])
print(pyladiesphb[0])

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 5 - Herança Multipla + Metodos especiais
* metodo especial __getitem__ na prática
'''
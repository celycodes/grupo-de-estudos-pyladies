class Pylady:
    def __init__(self, nome, membras):
        self.nome = nome
        self.membras = membras

    def __len__(self):
        return len(self.membras)

pyladiesphb = Pylady('PyLadies Parnaíba',['Celenny','Emilly','Vitória','Karina','Alinne','Ana'])
print(len(pyladiesphb))

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 5 - Herança Multipla + Metodos especiais
* metodo especial __len__ na prática
'''
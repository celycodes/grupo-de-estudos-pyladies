class Pyladies:
    def __init__(self, nome, integrantes, tem_homem ):
        self.nome = nome
        self.integrantes = integrantes
        self.tem_homem = tem_homem

    def __str__(self):
        return f'Membras: {self.integrantes}'

    def __len__(self):
        return len(self.integrantes)

    def __getitem__(self, item):
        return self.integrantes[item]

pyladiepi = Pyladies('Pyladies Piauí',['Celenny','Ana', 'Emily','Karina','Vitória', 'Alinne'], False)

print(pyladiepi[0])
print(pyladiepi)
print(len(pyladiepi))

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 5 - Herança Multipla + Metodos especiais
* Melhorando a classe Pyladies da aula 2 usando os métodos especiais.
'''
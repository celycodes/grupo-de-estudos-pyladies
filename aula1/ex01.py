'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 1 - aprendendo a criar classes, métodos e atributos
'''
class Pyladies:
    def __init__(self, nome, qtd_membros, tem_homem, integrantes):
        self.nome = nome
        self.qtd_membros = qtd_membros
        self.tem_homem = tem_homem
        self.integrantes = integrantes
        #print('atributos foram armazenados')

    def Dar_curso(self):
        print('para dar curso você precisa de ...')

    def Informacoes(self):
        print(f'\n{self.nome}\n{self.qtd_membros}\n{self.tem_homem}\n{self.integrantes}')

pyladies_buriti = Pyladies('PyLadies Buriti dos Lopes', 3, True, ['Celenny','kiko','Marco','Maju'])
pyladies_buriti.Informacoes()
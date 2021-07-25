'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 3 - usando o property
'''
class Pyladies:
    def __init__(self, nome,integrantes, nasc):
        self.__nome = nome
        self.__integrantes = integrantes 
        self.__nasc = nasc

    def GetNome(self):
        return self.__nome

    def SetNome(self,name):
        self.__nome = name.title()

    def GetInte(self):
        return self.__integrantes
    
    def SetInte(self, members):
        self.__integrantes = members

    @property
    def formatted(self):
        return f'-------------------------------------------------\n              DADOS DO CAPÍTULO   \n-------------------------------------------------\nNome: {self.__nome}\nIntegrantes: {self.__integrantes}\nData da fundação: {self.__nasc}\n-------------------------------------------------'

pyladies_buriti = Pyladies('PyLadies Buriti',['Celenny','kiko','Marco','Maju'], '15/10/2020')
print(pyladies_buriti.formatted)

class Pyladies:
    def __init__(self, nome, qtd_membros, integrantes):
        self.__nome = nome
        self.__qtd_membros = qtd_membros
        self.integrantes = integrantes
        self.__creators = {'Nome':[], 'E-mail':[]}
        self.__info_members = {'Nascimento':[], 'Universidade':[], 'Curso':[]}

    def GetNome(self):
        return self.__nome

    def SetNome(self,name):
        self.__nome = name.title()

    def GetQtd(self):
        return self.__qtd_membros

    def SetQtd(self, number):
        self.__qtd_membros = number
    
    def GetInte(self):
        return self.__integrantes
    
    def SetInte(self, members):
        self.__integrantes = members  
    
    def Getinfo(self):
        return self.__info_members
    
    def Setinfo(self, born, university, course):
        self.__info_members['Nascimento'].append(born)
        self.__info_members['Universidade'].append(university)
        self.__info_members['Curso'].append(course)

# OBS: classe Pyladies criada na aula 2 com algumas modificações como Nascimento, universidade e curso.
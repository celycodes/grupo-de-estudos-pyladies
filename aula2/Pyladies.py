class Pyladies:
    def __init__(self, nome, qtd_membros, tem_homem, integrantes):
        self.__nome = nome
        self.__qtd_membros = qtd_membros
        self.__tem_homem = tem_homem
        self.__integrantes = integrantes
        self.__creators = {'Nome':[], 'E-mail':[]}
        
    def GetNome(self):
        return self.__nome

    def SetNome(self, name):
        self.__nome = name.title()

    def GetQtd(self):
        return self.__qtd_membros

    def SetQtd(self, number):
        self.__qtd_membros = number
    
    def GetMen(self):
        return self.__tem_homem
    
    def SetMen(self, men):
        self.__tem_homem = men
    
    def GetInte(self):
        return self.__integrantes
    
    def SetInte(self, members):
        self.__integrantes = members

    def SetCreate(self, founder, mail):
        self.__creators['Nome'].append(founder)
        self.__creators['E-mail'].append(mail)  
    
    def GetCreate(self):
        if self.__creators['Nome'] == []:
            return None
        else:
            return self.__creators
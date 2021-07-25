import Marketing
import Conteudo

membras = [Marketing.Marketing('Cely', 'celypy@gmail.com'), Conteudo.Conteudo('Emilly', 'millypylady@hotmail.com')]

print('-=-       Perfil das Membras       -=-')
for lady in membras:
    lady.imprimir()

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 4 - polimorfismo + classes abstratas
'''
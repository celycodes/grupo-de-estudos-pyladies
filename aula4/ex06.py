import Programa as prog
import Filme as movie
import Serie as series

weekend = [prog.Programa('Fantástico'), movie.Filme('Avatar', '2h 42m'), series.Serie('Doctor Who', '12 temporadas'), prog.Programa('Domingão do Faustão') ,movie.Filme('Arrival', '1h 58m'), series.Serie('Mr. Robot', '4 temporadas')]

print('-=- Playlist Para Assistir da Cely -=-')
for program in weekend:
    program.printing()
print('-' * 40)

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 4 - polimorfismo + classes abstratas
'''
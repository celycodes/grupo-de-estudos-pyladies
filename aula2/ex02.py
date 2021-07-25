'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 1 - aprendendo a criar classes, métodos e atributos
'''
from Pyladies import Pyladies

pyladies_buriti = Pyladies('PyLadies Buriti', 3, True, ['Celenny','kiko','Marco','Maju'])

pyladies_buriti.SetCreate('Celenny', 'celennycs@gmail.com')

print(pyladies_buriti.GetNome())
print(pyladies_buriti.GetQtd())
print(pyladies_buriti.GetCreate())
pyladies_buriti.SetNome('BURITI')
print(pyladies_buriti.GetNome())
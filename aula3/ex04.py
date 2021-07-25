'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 3 - desafio ex04
'''
from classepyladies import Pyladies

pyladies_buriti = Pyladies('PyLadies Buriti', 3,['Celenny','Marco','Maju'])

pyladies_buriti.Setinfo('24/11/2001', 'Uespi', 'Ciência da computação')
pyladies_buriti.Setinfo('29/11/2003', 'Uespi', 'Letras')
pyladies_buriti.Setinfo('28/11/2002','Ufdpar', 'Moda')

print(pyladies_buriti.Getinfo())
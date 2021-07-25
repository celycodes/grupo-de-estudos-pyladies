class Fsociety(object):
    def __call__(self):
        return 'Hello Friend!'
    
elliot = Fsociety()

print(elliot())

'''
Exercícios do grupo de estudos de python 
intermediário da PyLadies Brasil (POO) 
AULA 5 - Herança Multipla + Metodos especiais
* metodo especial __call__ na prática
- usado quando o objeto é invocado como uma função.
'''
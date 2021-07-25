class Animal:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.classe = None
        self.especie = None

    def get_info(self):
        print('-='*13)
        print('Informações:\n')
        print(f'Nome:{self.nome}\nPeso:{self.peso}kg\nAltura:{self.altura}cm\nClasse:{self.classe}\nEspecie:{self.especie}')
        print('-='*13)

    def comer(self):
        print(f'O {self.nome} está comendo ...')
    
    def andar(self):
        print(f'O {self.nome} está andando ...')
   
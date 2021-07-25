import PyladiesParnaiba as pyphb

class Conteudo(pyphb.PyladiesParnaiba):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def pasta(self):
        print(f'Pasta: Conteúdo')

    def funçao(self):
        print(f'Função: Cria os conteudos mensais do grupo como Palestras, Lives, Workshops, Mesas redondas, Videos.')


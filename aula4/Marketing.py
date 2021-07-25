import PyladiesParnaiba as pyphb

class Marketing(pyphb.PyladiesParnaiba):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def pasta(self):
        print(f'Pasta: Marketing')

    def funçao(self):
        print(f'Função: Cuida das redes sociais da pyladies, cria as artes dos produtos, postagens e eventos')
    
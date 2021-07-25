import Programa as prog

class Filme(prog.Programa):
    def __init__(self, nome, duraçao):
        super().__init__(nome)
        self.duraçao = duraçao

    def printing(self):
        print(f'Filme: {self.nome} | Duração: {self.duraçao}')
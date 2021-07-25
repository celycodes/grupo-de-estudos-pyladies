import Programa as prog

class Serie(prog.Programa):
    def __init__(self, nome, temporadas):
        super().__init__(nome)
        self.temporadas = temporadas
    
    def printing(self):
        print(f'Série: {self.nome} | Temporada(s):{self.temporadas}')

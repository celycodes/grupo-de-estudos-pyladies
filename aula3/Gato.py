import Animal as an

class Gato(an.Animal):
    def __init__(self,nome,peso,altura):
        super().__init__(nome,peso,altura)
        self.classe = 'Mamíferos'
        self.especie = 'Gato'
    
    def ronronar(self):
        print('rrrrrr! rom-rom! rrrrrr! rom-rom!')
    
    def miar(self):
        print('miau! miau! miau! miau!')


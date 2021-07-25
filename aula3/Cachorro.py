import Animal as an

class Cachorro(an.Animal):
    def __init__(self,nome,peso,altura):
        super().__init__(nome,peso,altura)
        self.classe = 'Mamifero'
        self.especie = 'Cachorro'
    
    def Latir(self): 
        print('au au !')
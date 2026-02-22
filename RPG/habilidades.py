from random import choice
class Hab:
    def __init__(self):
        self.lista = []
    
    def adicionar(self):
        elementos = ['Fogo','Agua','Vento','2','4','5']
        golpes = ['Bola de' , 'Missel de' , 'Cometa de']
        for _ in range(5):
            habilidade = f'{choice(golpes)} {choice(elementos)}'
            self.lista.append(habilidade)
        
        print(self.lista)

Hab().adicionar()
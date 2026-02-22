class Tipo_classe:
    def __init__(self,hp,mana,dano,icone):
        self.nivel = 1
        self.hp = hp
        self.mana = mana
        self.dano = dano
        self.icone = icone

class Lutador(Tipo_classe):
    def __init__(self):
        super().__init__(hp=500,mana=200,dano=50,icone="guerreiro")

class Mago(Tipo_classe):
    def __init__(self):
        super().__init__(hp=250,mana=500,dano=48,icone="mago")


class Arqueiro(Tipo_classe):
    def __init__(self):
        super().__init__(hp=280,mana=280,dano=100,icone="arqueiro")


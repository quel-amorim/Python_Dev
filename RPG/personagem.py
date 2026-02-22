class Jogadores:
    def __init__(self):
        self.players = []
    
    def adicionar(self):
        while True:
            try:
                x = int(input('Quantos personagem criar ? '))
                break
            except ValueError:
                print('Digitou alguma coisa de errado !')
                continue
        
        for i in range(x):
            nome = input('Nome do Personagem : ')
            personagens = {"ID" : i+1 , "Personagem" : nome}
            self.players.append(personagens)
            i+=1
        
        print(self.players)
    
    
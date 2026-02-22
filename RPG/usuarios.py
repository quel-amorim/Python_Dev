import json
class Usuarios:
    def __init__(self):
        self.lista = []
        self.verifcar_json()

    def registar(self):
        while True:
            try:
                a = int(input('Criar quantos usuarios ?'))
                break
            except ValueError:
                print('Volte erro de digitação somente int ex: 1,2,3 ...')
                continue

        for _ in range(a):
            username = input('nome para seu usuario :')
            email = input('email de contato :')
            senha = input('senha para conta :')
            cliente = {"UserName" : username , "Email" : email , "Password" : senha}
            self.lista.append(cliente)
        
        print('Feito !')
        self.json()
    
    def verifcar_json(self):
        try:
            with open('usuarios.json','r') as json_arquivos:
                self.lista = json.load(json_arquivos)
        except FileNotFoundError:
            self.lista = []
    
    def json(self):
        if not self.lista:
            pass
        else:
            with open('usuarios.json','w')as json_arquivos:
                json.dump(self.lista , json_arquivos , indent=4)
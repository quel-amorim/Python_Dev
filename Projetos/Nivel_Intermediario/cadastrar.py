"""
    Criar , editar e remover usuarios , login e senha , salvar json ou sqlite
"""
import json

class Login:
    def __init__(self):
        self.meus_usuarios = []
        self.verificar()

    def verificar(self):
        global meus_usuarios
        try:
            with open('dados_usuarios.json','r') as arquivo_json:
                self.meus_usuarios = json.load(arquivo_json)
        except FileExistsError:
            self.meus_usuarios = []
    
    def salvar(self):
        if not self.meus_usuarios:
            pass
        else:
            with open('dados_usuarios.json','w') as arquivo_json:
                json.dump(self.meus_usuarios , arquivo_json , indent=4)

    def registar(self):
        login = input('registrar um nome de usuario :')
        senha = input('cadastra senha :')

        usuarios = {"Login" : login , "Senha" : senha}
        self.meus_usuarios.append(usuarios)
        self.salvar()
    
Login().registar()
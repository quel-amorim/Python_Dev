"""
    Criar , editar e remover usuarios , login e senha , salvar json ou sqlite
"""
import json

class Usuario:
    def __init__(self):
        self.usuarios = []
    
    def criar(self):
        while True:
            try:
                x = int(input('Cadastrar quantos usuarios ?'))
                break
            except ValueError:
                return "Erro de ditação"
        
        for _ in range(x):
            username = input('Nome de usuario :')
            __senha = input('Senha :')
            cliente = {"ID N#": len(self.usuarios)+1,"Usuario" : username ,"Senha" : __senha}
            self.usuarios.append(cliente)
        
        print('usuarios cadastrado com sucesso !')
        self.salvar()
    
    def salvar(self):
        if not self.usuarios:
            pass
        else:
            with open('usuarios.json','w') as arquivo_json:
                json.dump(self.usuarios,arquivo_json,indent=4)
    

class Login(Usuario):
    def __init__(self):
        super().__init__()
        self.verificar()
    
    def verificar(self):
        try:
            with open('usuarios.json','r') as arquivo_json:
                self.usuarios = json.load(arquivo_json)
        except FileNotFoundError:
            self.usuarios = []
    
    def exibir(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\n=== USUÁRIOS CADASTRADOS ===")
        for usuario in self.usuarios:
            print(f"ID: {usuario.get('ID N#')}")
            print(f"Usuário: {usuario.get('Usuario')}")
            print("-" * 30)

Login().exibir()
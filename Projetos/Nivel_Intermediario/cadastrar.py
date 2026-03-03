"""
    Criar , editar e remover usuarios , login e senha , salvar json ou sqlite
"""
import json

class Usuario:
    def __init__(self):
        self.usuarios = []
        self.verificar() # ele ler se tem algum dado salvo , importante nas partes de editar e remover usuarios !
    
    def verificar(self):
        try:
            with open('usuarios.json','r') as arquivo_json:
                self.usuarios = json.load(arquivo_json)
        except FileNotFoundError:
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
            cliente = {"ID": len(self.usuarios)+1,"Usuario" : username ,"Senha" : __senha}
            self.usuarios.append(cliente)
        
        print('usuarios cadastrado com sucesso !')
        self.salvar()
    
    def salvar(self):
        if not self.usuarios:
            pass
        else:
            with open('usuarios.json','w') as arquivo_json:
                json.dump(self.usuarios,arquivo_json,indent=4)
    
    def remover(self):
        if not self.usuarios:
            print('Não tem usuarios para remover')
            return
        
        print('\nUsuarios Encontrados :')
        for cliente in self.usuarios:
            print(f'ID {cliente['ID']} -> {cliente['Usuario']}')

        try:
            id_remover = int(input('Diga o id de usuario que deseja excluir :'))
        except ValueError:
            return "Id desconhecido !"
        
        usuarios_encontrados = False
        for cliente in self.usuarios:
            if cliente["ID"] == id_remover:
                self.usuarios.remove(cliente)
                usuarios_encontrados = True
                print('Usuario removido')
                break
        
        if not usuarios_encontrados:
            print('ID desconhecido')
            return

        for i , cliente in enumerate(self.usuarios):
            cliente["ID"] = i+1
        
        self.salvar()
    
    def editar(self):
        if not self.usuarios:
            print('Não tem usuarios para editar')
            return
        
        print('\nUsuarios Encontrados :')
        for cliente in self.usuarios:
            print(f"ID {cliente['ID']} -> {cliente['Usuario']}")

        try:
            id_editar = int(input('Diga o ID do usuario que deseja editar :'))
        except ValueError:
            return "ID inválido!"
        
        usuario_encontrado = False

        for cliente in self.usuarios:
            if cliente["ID"] == id_editar:
                usuario_encontrado = True
                
                novo_usuario = input('Novo nome de usuario (deixe vazio para não alterar): ')
                nova_senha = input('Nova senha (deixe vazio para não alterar): ')
                
                if novo_usuario:
                    cliente["Usuario"] = novo_usuario
                
                if nova_senha:
                    cliente["Senha"] = nova_senha
                
                print('Usuario editado com sucesso!')
                break
        
        if not usuario_encontrado:
            print('ID não encontrado')
            return
        
        self.salvar()



class Login(Usuario):
    def __init__(self):
        super().__init__()
        self.verificar()
    
    def exibir(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\n=== USUÁRIOS CADASTRADOS ===")
        for usuario in self.usuarios:
            print(f"ID: {usuario.get('ID N#')}")
            print(f"Usuário: {usuario.get('Usuario')}")
            print("-" * 30)

Usuario().remover()
"""Programa para listar tarefas do seu interece , tendo funções de adicionar , listar e remover tarefas também salvar como arquivo txt. ou json."""
import json
# Começar Tarefas

tarefas = []

def adicionar():
    tarefas_listadas = 0
    while True:
        try:
            x = int(input('Adicionar quantas tarefas ?'))
            break
        except ValueError:
            return "Erro de sintace"
    
    for _ in range(x):
        nome = input('Nome da sua Tarefa :')
        tarefa_ativa = int(input('A tarefa foi feita ?\n[1] SIM\n[2] NÃO\nEscolha :'))
        
        if tarefa_ativa == 1:
            criados = {"ID" : tarefas_listadas+1 ,"Tarefa" : nome , "Atividade" : "Concluido"}
            tarefas.append(criados)
        else:
            criados = {"ID" : tarefas_listadas+1 ,"Tarefa" : nome , "Atividade" : "Pedente"}
            tarefas.append(criados)
    
    print('Tarefas Listadas :' + str(tarefas_listadas))
    

def salvar_arquivo():
    if not tarefas:
        print('Nada para salvar')
    else:
        with open('tarefas_registradas.json','w') as arquivo_json:
            json.dump(tarefas,arquivo_json,indent=4)

def verificar():
    try:
        with open('tarefas_registradas.json','r') as arquivo_json:
            tarefas = json.load(arquivo_json)
    except FileNotFoundError:
            tarefas = []

def exibir():
    if not 'tarefas_registradas.json':
        print('Não tenho nada para mostra !')
    else:
        print('Lista encontrada')
       

def remover():
    id_remocao = int(input('Diga qual ID você quer remover ?'))


while True:
    verificar() # Ele vai ser o primeiro porque ele vai ver se tem algum arquivo salvo , para não carregar dados novos apagando os velhos
    print('-'*5)
    print('Programa de Tarefas')
    print('-'*5)
    print('[1] Adicionar Tarefas')
    print('[2] Salvar')
    print('[3] Exibir')
    print('[4] Remover')
    escolha = input('Escolha :')

    match escolha:
        case "1":
            adicionar()
        case "2":
            salvar_arquivo()
            break
        case "3":
            exibir()
        
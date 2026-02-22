from random import randint
partidas = 0
pontos_x = 0
pontos_y = 0
#
historico = []

print('-=-'*10)
print('Jogo de Acerta o número da máquina')
print('-=-'*10)
qts = int(input('Rodar até quantas vezes ?'))
for _ in range(qts):
    x = randint(1 , 5)
    y = randint(1 , 5)
    resultados = {"Partida" : partidas+1 ,"Jogador" : x , "Maquina" : y}
    historico.append(resultados)
    print(f'\n{partidas+1} | Jogador {x} vs  Maquina {y}')
    partidas +=1
    if x == y:
        pontos_x+1
        historico.append(pontos_x)
        pontos_x +=1
    else:
        pontos_y+1
        historico.append(pontos_y)
        pontos_y +=1

print('\nPontuacao')
print('Jogador :', pontos_x)
print('Maquina :' , pontos_y)
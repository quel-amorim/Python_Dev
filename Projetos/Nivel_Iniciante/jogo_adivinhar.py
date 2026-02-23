"""
    Programa consiste fazer o computador gerar um número aleátorio e contar as tentativas
 """
from random import randint
import json
partidas = []
def partidas_salvas():
    if not partidas:
        pass
    else:
        with open('partidas.json','w') as json_arquivo:
            json.dump(partidas,json_arquivo,indent=4)


qts = int(input('Quer tentar até quantas vezes ?'))

total_partidas = 0
vitorias_jogador = 0

for total_partidas in range(qts):
    sistema = randint(1,5)
    jogador = int(input('Tente acertar o número que a maquina está pensando: '))

    historico_partidas = {
        "Partida N#": total_partidas + 1,
        "Jogador jogou": jogador,
        "Sistema pensou": sistema
    }

    partidas.append(historico_partidas)
    partidas_salvas()

    if jogador == sistema:
        print('Finalmente o JOGADOR ACERTOUUUUUUUUUU !')
        vitorias_jogador += 1

print(f'No total de {qts} tentativas, o jogador acertou: {vitorias_jogador}')
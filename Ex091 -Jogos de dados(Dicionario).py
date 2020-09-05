#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o
#vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador1' : randint(1,6), 'Jogador2' : randint(1,6),'Jogador3' : randint(1,6),'Jogador4' : randint(1,6)}

print(f"{'ROLAGENS':-^30}")
for k, v in jogos.items():
    print(f"{k} tirou no dado {v}")
    sleep(0.5)

print(f"{'COLOCAÇÃO':-^30}")
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f"{k+1}ºLugar-> {v[0]} tirou no dado {v[1]}")
    sleep(0.5)
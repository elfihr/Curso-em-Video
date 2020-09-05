#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
#vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
listao = {}
soma = 0
partidas = []
listao['JOGADOR'] = str(input("->NOME DO JOGADOR: "))
n = int(input(f"->Quantas partidas {listao['JOGADOR']} jogou? "))
for c in range(0,n):
    partidas.append(int(input(f"->Quantos gols marcou na partida {c+1}º: ")))
listao['Gols por Partida'] = partidas[:]
listao['Total'] = sum(partidas)

print(f"{'TIPO 1':-^30}")
print(listao)

print(f"\n{'TIPO 2':-^30}")
print(f"O jogador {listao['JOGADOR']} jogou {n} partidas.")
for k, v in listao.items():
    print(f"->O valor {k} tem {v}")
print(f"\n{'TIPO 3':-^30}")
print(f"O jogador {listao['JOGADOR']} jogou {n} partidas")
for k, v in enumerate(partidas):
    print(f"     =>Na partida {k} marcou {v} gols")
print(f"Foi um total de {listao['Total']} gols")
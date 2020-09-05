#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador.

#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
#vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
sistema = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input("NOME: "))
    n = int(input("PARTIDAS JOGADAS: "))
    for c in range(0, n):
        gols.append(int(input(f"Gols da parida {c+1}º: ")))
    jogador['partidas'] = n
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    sistema.append(jogador.copy())

    while True:
        resp = str(input("Quer continuar?[S/N]: ")).upper()[0]
        if resp in "NS":
            break
        print("ERROR")
    if resp in "N":
        break

print('-'*60)
print(f'{"TABELA":^60}')
print('-'*60)
print('Nº',end=" ")
for p in jogador.keys():
    print(f"{p:<12}",end=" ")
print()
for k,v in enumerate(sistema):
    print(f"{k:<5}",end=" ")
    for n in v.values():
        print(f"{str(n):<12}",end=" ")
    print()
print('-'*60)

for j in sistema:
    while True:
        r = int(input("Que jogador você quer ver o desempenho?[999 para]:"))
        if r == 999:
            break
        if r >= len(jogador):
            print("ERROR 404")
        else:
            print(f"{sistema[1]['Nome']}",end=' ')
            for k,v in enumerate(sistema[r]['Gols']):
                print(f"No jogo {k} ele fez {v} gols")
print('-'*60)
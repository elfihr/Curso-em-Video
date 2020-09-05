#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador.

#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
#vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
sistema = []
jogador = {}
gol = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input("NOME: "))
    part = int(input("PARTIDAS JOGADAS: "))
    for p in range(0,part):
        gol.append(int(input(f"SALDO DE GOLS DA PARTIDA {p+1}º: ")))
    jogador['Gols por Partida'] = gol[:]
    jogador["Saldo Total"] = sum(gol)
    sistema.append(jogador.copy())
    gol.clear()

    while True:
        resp = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
        if resp in "NS":
            break
        print("ERROR 404")
    if resp in "N":
        break

print('-='*30)
print(f'{"SISTEMA":^60}')
print('-='*30)
for c in jogador.keys():
    print(f"{c:<15}",end=" ")
print()
print('-'*60)
print("Nº")
for k, v in enumerate(sistema):
    print(f"{k:<5}",end=" ")
    for n in v.values():
        print(f"{str(n):<15}",end=" ")
    print()
print('-'*60)






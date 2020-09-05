#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
# jogo, cadastrando tudo em uma lista composta.
from random import randint
sorteio = []
temp = []
tot = 0
print("=-"*50)
print(f"{'BOLÃO DO FAUSTÃO':^100}")
print("=-"*50)
n = int(input("Quantos sorteios você quer fazer?: "))
while tot <= n:
    cont = 0
    while True:
        sor = randint(1, 61)
        if sor not in temp:
            temp.append(sor)
            cont += 1
        if cont >= 6:
            break
    sorteio.append(temp[:])
    temp.clear()
    tot += 1

for i, v in enumerate(sorteio):
    print(f"JOGO: {i+1} -> {v}")






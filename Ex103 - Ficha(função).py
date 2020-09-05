#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido informado corretamente.


#LOCAL
def ficha(n="", g=0):
    return f"JOGADOR: {n}" \
           f"\nGols Marcados: {g}"


#GLOBAL
nom = str(input("NOME: "))
gol = str(input("GOLS: "))
if nom == "".strip():
    nom = "Nome não prenchido"
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

f = ficha(nom, gol)
print('-'*20)
print(f)
print('-'*20)
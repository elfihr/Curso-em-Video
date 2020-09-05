#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

#LOCAL
def voto(a):
    from datetime import date
    t = date.today().year - n
    if t >= 16 or t < 18:
        return f"A pessoa com {t} anos tem voto OPCIONAL"
    elif t >= 18:
        return f"A pessoa com {t} anos tem voto OBRIGATORIO"
    else:
        return "A pessoa com {t} anos tem voto NEGADO"


#PRINCIPAL
n = int(input(f'Qual seu ano de nascimento? '))
v = voto(n)
print(v)
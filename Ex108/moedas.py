def aumentar(num=0, porc=0):
    res = num*(porc * 0.01)+num
    return f"{res:.2f}"


def diminuir(num=0, porc=0):
    res = num - num*(porc * 0.01)
    return f"{res:.2f}"


def dobro(num=0):
    res = num*2
    return f"{res:.2f}"


def metade(num=0):
    res = num/2
    return f"{res:.2f}"


def monetario(num=0,moeda='R$'):
    return f"{moeda}{num}".replace('.',',')


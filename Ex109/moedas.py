def aumentar(num=0, porc=0, convert=False):
    """
    :param num: Numero selecionado para conversão
    :param porc: Porcentagem a e ser escolhida pelo usuario
    :param convert: Ativar formatação monetaria
    :return: Valor retornado
    """
    res = num*(porc * 0.01)+num
    return res if not convert else monetario(res)


def diminuir(num=0, porc=0, convert=False):
    res = num - num*(porc * 0.01)
    return res if not convert else monetario(res)


def dobro(num=0, convert=False):
    res = num*2
    return res if not convert else monetario(res)


def metade(num=0, convert=False):
    res = num/2
    return res if not convert else monetario(res)


def monetario(num=0,moeda='R$'):
    return f"{moeda}{num:.2f}".replace('.',',')


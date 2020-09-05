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


def resumo(res = 0,porc= 0):
    print('-' * 40)
    print(f"{'CONVERSÃO MONETÁRIA'.center(40)}")
    print('-' * 40)
    print(f'Valor Selecionado {monetario(res)}')
    print(f"O Aumento em {porc}% elevara para \t\t{aumentar(res,porc,True)}")
    print(f"A Diminuição em {porc}% reduzira para \t{aumentar(res, porc, True)}")
    print(f"O dobro de {monetario(res)} é \t\t\t\t{dobro(res,True)}")
    print(f"A metade de {monetario(res)} é \t\t\t{metade(res,True)}")

    print('-' * 40)

def aumentar(num, porc):
    res = num*(porc * 0.01)+num
    return f"R${res:.2f}"


def diminuir(num, porc):
    res = num - num*(porc * 0.01)
    return f"R${res:.2f}"


def dobro(num):
    res = num*2
    return f"R${res:.2f}"


def metade(num):
    res = num/2
    return f"R${res:.2f}"


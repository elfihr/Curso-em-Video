#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#LOCAL
def fatorial(a, show=False):
    """
    :param a: Numero Fatorial
    :param show: True para mostrar a a equação
    :return: O que será printado na tela
    """
    cont = a
    total = 1
    while cont > 0:
        if show:
            print(a,end='')
            print(f' X ' if cont > 1 else " = ",end='')
        total *= a
        cont -= 1
        a -= 1
    return total


#PRINCIPAL
help(fatorial)


f = int(input("Digite o numero para realizar a operação fatorial: "))

f1 = fatorial(f,show=True)
print(f"{f1}")
#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

#LOCAL
def turma(* n):
    """
    Realiza media da Turma
    :param n: Notas armazenadas
    :return: retorna o dicionario
    """
    classe = {}
    classe['Notas Registradas'] = len(n)
    classe['Maior'] = max(n)
    classe['Menor'] = min(n)
    classe['Media'] = sum(n)/len(n)
    return classe


#Global

tot = turma(9.2,1.1,9.4)
print(tot)
help(turma)
#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
#(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
#contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
sistema = {}

sistema['Nome'] = str(input("->NOME: "))

idade = int(input("->ANO DE NASCIMENTO: "))
sistema['Idade'] = date.today().year - idade

sistema['CTps'] = int(input("->Nº[0 não tem]: "))
if sistema['CTps'] == 0:
    sistema['CTps'] = "Não tem"
else:
    sistema['Ano da Contratação'] = int(input("->ANO DA CONTRATAÇÃO: "))
    sistema['Aposentadoria'] = sistema['Idade'] + (35 - (date.today().year - sistema['Ano da Contratação']))
    sistema['salario'] = float(input("->SALARIO R$: "))

print("=-"*15)
print(f"{'DADOS':^30}")
print("=-"*15)
for k, v in sistema.items():
    print(f"->{k} - {v}")



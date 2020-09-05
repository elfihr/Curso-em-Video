#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
#dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['Nome'] = str(input("NOME: "))
aluno['Média'] = int(input("MEDIA: "))
if aluno['Média'] >= 7:
    aluno['Situação'] = "Aprovado"
elif aluno['Média'] <= 6.9 or aluno['Média'] >= 5:
    aluno['Situação'] = "Recuperação"
else:
    aluno['Média'] = "Recuperação"
print('-='*20)
print(f'{"MEDIA FINAL":^40}')
print('-='*20)
print(f"->Aluno: {aluno['Nome']:<20}")
print(f"->Média: {aluno['Média']:<20}")
print(f"->Situação: {aluno['Situação']:<20}")
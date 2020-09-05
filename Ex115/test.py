from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ler Arquivo','Cadastro','Sair do Programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Opção 3')
        break
    else:
        print('\033[1;33mDigite uma opção válida\033[m')
    sleep(1)
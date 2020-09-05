#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
def escreve(msg):
    t = len(msg) + 4
    print(f"{'-':<15}".strip()*t)
    print(f"  {msg}")
    print(f"{'-':>15}".strip()*t)

txt = str(input("Digite uma palavra ou texto: "))
escreve(txt)
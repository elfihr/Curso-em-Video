r = 0
choice = 4
while choice == 4 or choice >= 6:
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    choice = int(input("Qual operação aritmetica você quer fazer?\n[1]SOMAR\n[2]Multiplicar\n[3]Maior\n[4]Refazer escolha\n[5]Sair do programa\nESCOLHA: "))
    if choice >= 6:
        print("Escolha inexistente. Tente de novo.")
    if choice == 4:
      print("Digite os números novamente")

if choice == 1:
    r = n1 + n2
    print("O resultado foi {}".format(r))
if choice == 2:
    r = n1 * n2
    print("O resultado foi {}".format(r))
if choice == 3:
    if n1 > n2:
         print("O primeiro - {} - número é maior que o segundo número - {} -".format(n1, n2))
    else:
        print("O segundo número - {} - é maior que o primeiro número - {} -".format(n2, n1))
if choice == 5:
    print("Obrigado por testar o programa, volte sempre")

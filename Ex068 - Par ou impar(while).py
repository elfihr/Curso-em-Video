import random
print("=-"*20)
print("          JOGO DO ÍMPAR/PAR")
print("=-"*20)
game = choice = " "
n = machine = total = v = 0
while True:
    n = int(input("Escolha um numero inteiro[1 a 10]: "))
    machine = random.randint(1, 10)
    game = str(input("Escolha ímpar ou par[P/I]: ")).upper().strip()[0]
    while game not in "PI":
        game = str(input("Escolha ímpar ou par[P/I]: ")).upper().strip()[0]
    total = machine + n
    print(f"Você jogou {n} e o computador jogou {machine}\nO total do somatorio é {total}")
    if game == "P" and total % 2 == 0:
        print("Deu par!")
        print(f"Voce venceu o jogo com {v}º vitoria(s)")
        choice = str(input("Vamos novamente[S/N]?: ")).upper().strip()[0]
        if choice == "N":
            break
    if game == "I" and total % 2 != 0:
        print("Deu ímpar!")
        print(f"Voce venceu o jogo com {v}º vitoria(s)")
        choice = str(input("Vamos novamente[S/N]?: ")).upper().strip()[0]
        if choice == "N":
            break
    else:
        if total % 2 == 0:
            print("Deu par! O computador venceu o jogo")
        else:
            print("Deu ímpar! O computador venceu o jogo")
        break
print("=-"*20)
print("            Obrigado por jogar")



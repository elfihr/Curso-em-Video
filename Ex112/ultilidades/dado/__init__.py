def leiaDinheiro(msg):
    validade = False
    while not validade:
        enter = str(input(msg)).replace(',','.').strip()
        if enter.isalpha() or enter == "":
            print(f"\033[1;31m \"{msg}\" não é um número válido\033[m")
            #O parentes de msg com barra sefez nescessario
        else:
            validade = True
            return float(enter)

import random
cont = 0
print("\033[1;35m=-=-=-=-=-Sou a SKYNET!=-=-=-=-=-\nVou conquistar o mundo!!\nSe quer me impedir tente adivinha um numero de 0 a 10 em menos de 4 tentativas\nmuahahuauhahahau")
pc = random.randint(0, 10)
n = int(input("Digite um numero de 0 a 10: "))
while n != pc and cont < 4:
    cont += 1
    if n > pc:
        n = int(input("Um numero menor!Tente de novo, essa é sua {}º vez".format(cont)))
    else:
        n = int(input("Um numero maior!Mais uma vez!!Essa é sua {}º vez".format(cont)))

if cont >= 4:
    print("Eu venci!Humano!")
else:
    print("Nãaao!!Malditos salgadinhos!!")


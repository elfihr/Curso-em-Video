list = ("Exercício", "Python", "programa", "tupla", "palavras" ,"acentos", "vogais")

for p in list:
    print(f"\nA palavra {p.upper()} temos", end=" ")
    for list in p:
        if list.lower() in "aeiou":
            print(f"{list}", end=" ")
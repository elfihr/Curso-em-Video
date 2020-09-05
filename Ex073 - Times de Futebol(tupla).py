# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ("Palmeiras", "Flamengo", "Grêmio", "Cruzeiro", "Santos", "Atlético",
         "Corinthians", "Internacional", "Bahia", "Chapecoense")

print("-=" * 50)

print("Quais são os 5 primeiros colocados:")
print(f" {times[:5]} ")

print("\nQuais os últimos colocados 4 colocados?: ")
print(f" {times[-4:]}")

print("\nTimes em ordem alfabetica?: ")
print(sorted(times))

print("\nEm que posição esta a chape?: ")
print(f"Chapecoense está na posição {times.index('Chapecoense')+1}º posição")

print("-=" * 50)
from random import sample
number = tuple(sample(range(10), 5))
print(f"Os numeros sorteados foram {number}")
print("O maior valor foi {} e o menor valor {}".format(max(number), min(number)))
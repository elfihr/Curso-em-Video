from random import randint
t = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10) ))
print(f"Sorteei os valores:")
for n in t:
    print(f"{n}", end=" ")
print("\nO maior valor é:")
print(f"->{max(t)}")
print(f"->{min(t)}")
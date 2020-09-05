import random
n = int(input("\033[1;32mPense num número de 0 a 5: "))
r = random.randint(0, 5)
if n == r:
    print("\033[4;35mCaramba! Parece até que você lê mentes :O")
else:
    print("\033[4;35mnão foi dessa vez, tente novamente =(")
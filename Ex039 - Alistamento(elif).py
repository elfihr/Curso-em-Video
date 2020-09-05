i = int(input("\033[1;32mQual é a sua idade? " ))

if i < 18:
    i1 = 18 - i
    print("\033[1;34mAinda falta {} anos para se alistar".format(i1))
elif i > 18:
    i1 = i - 18
    print("\033[1;35mVocê ja deve ter se alistado ja que se passou {} anos do alistamento".format(i1))
else:
    print("\033[1;32mCorre moleque! Ta na hora de se alistar")
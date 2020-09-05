
c = ('\033[m',
      "\033[0;30;44m",
     '\033[0;30;45m')


def doctor(h):
    print(c[2])
    return help(h)




def efeito(msg, cor = 0):
    tam = len(msg) +4
    print(c[cor],end='')
    print('-'*tam)
    print(f"  {msg}")
    print('-' * tam)
    print(c[0], end='')

while True:
    efeito("PYTHON DOCTOR HELP",1)
    d = str(input("->Qual ferramenta você que saber[999 para]?" ))
    if d == "999":
        print(f"Fim do Programa",2)
        break
    else:
        doctor(d)

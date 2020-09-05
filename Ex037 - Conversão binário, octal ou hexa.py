n = int(input("Digite um numero inteiro para conversao: "))
op = int(input('''Digite o numero para escolher a conversão:
[1]binario
[2]octal
[3]hexadecimal 
>>>>'''))

if op == 1:
    print("O numero convertido para binario é {}".format(bin(n)[2:]))
elif op == 2:
    print("O numero convertido para octal é {}".format(oct(n)[2:]))
elif op == 3:
    print("O numero convertido para hexadecimal é {}".format(hex(n)[2:]))
else:
    print("ERROR!!Digite uma opção valida!")
c = float(input("\033[1;34mQual o valor da casa? "))
s = float(input("\033[1;35mQual o seu salário?: "))
a = float(input("\033[1;32mQuantos anos você pretende quitar a dívida? "))

p = a * 12
v = c / p
print("\033[1;34mSerão {} parcelas no valor de {:.2f}".format(p, v))

if v >= 0.3 * s:
    print("\033[1;35mDesculpe, não podemos fazer o emprestimo.")
else:
    print("\033[1;35mParabêns!! Você foi aprovado!")
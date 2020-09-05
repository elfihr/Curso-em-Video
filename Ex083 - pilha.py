#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use
#parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
#fechados na ordem correta.
pull = []
print("Digite uma expressão")
exp = str(input("--> " ))
for simb in exp:
    if simb == "(":
        pull.append('(')
    elif simb == ")":
        if len(pull) > 0:
            pull.pop()
        else:
            pull.append(')')
            break
if len(pull) == 0:
    print("Voce colocou todos os parenteses")
else:
    print("A solução não foi fechada corretamente")

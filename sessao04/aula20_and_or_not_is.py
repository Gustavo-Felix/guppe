'''
 'and' precisa que os dois valores estejam 'True'
 'or' necessita de apenas um dos valores seja 'True'
 'not' o valor do booleano é invertido
 'is' o valor é comparado com um segundo valor
'''

ativo = False
logado = False

if ativo:
    print("Bem-Vindo usuário!")
else:
    print("Você precisa estar ativo, por favor cheque seu e-mail!")

print(ativo is True)
print(ativo is False)







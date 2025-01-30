"""
numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno do pop: {ret}')

ret_pr = print(numeros)

print(f'Retorno do print: {ret_pr}')

# Primeira função

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(ret)

def diz_oi():
    return 'Oi'

alguem = ' Pedro!'

print(diz_oi() + ',' + alguem)

# Exemplo 01 - Só é executado as coisas antes do RETURN

def diz_oi():
    print('Estou executando antes do "oi"')
    return 'Oi!'
    print('Estou executando depois do "oi"')

print(diz_oi())

# Exemplo 02

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 03

def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Funcao cara ou coroa

from random import random

def joga_moeda():
    # Gera 0 ou 1
    if random() < 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
"""

# Erros comuns em uma função

def impar():
    num = 5
    if num % 2 != 0:
        return True
    return False

print(impar())




















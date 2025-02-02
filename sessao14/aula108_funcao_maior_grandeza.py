"""
# Exemplo 01

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(4, 2, soma))
print(calcular(4, 2, subtracao  ))
print(calcular(4, 2, multiplicacao))
print(calcular(4, 2, divisao))

# Nested Functions

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Oi, ', 'Sai Daqui, ', 'Olá, '))
    return humor() + pessoa

print(cumprimento('Joao'))


# Retornando funções de outras funções

from random import choice

def rir():
    def risada():
        return choice(('hahahh', 'kkkkkkkk', 'rs'))
    return risada

rindo = rir()

print(rindo())

"""
from random import choice

def faz_rir(pessoa):
    def fazendo_rir():
        risada = choice(('kkkkkkkkk', 'hahahhaah', 'rsrsrsrs'))
        return f'{pessoa} {risada}'
    return fazendo_rir

rindo = faz_rir('Gustavo')
print(rindo())
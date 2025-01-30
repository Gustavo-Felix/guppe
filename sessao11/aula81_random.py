"""
# Exemplo 01 - Importando todo o modulo - Não Recomendavel

import random

n = random.random() # Gera um número entre 0 e 1

if n > 0.5:
    print('Cara')
else:
    print('Coroa')

# Exemplo 02

from random import random # Importando apenas a função random() - Recomendado

for i in range(10):
    print(random())

# Função uniform - Um Valor aleatório em valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(0, 10))

# Função randint - Um Valor pseudo-aleatório em valores estabelecidos - NÚMEROS INTEIROS - Pode Vir Repetidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')


# Função choice - Valor aleatório de um iterável

from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']

print(choice(jogadas))
"""

# Função shuffle - Embaralha Dados

from random import shuffle

jogadas = ['Pedra', 'Papel', 'Tesoura']
print(jogadas)

shuffle(jogadas)

print(jogadas)










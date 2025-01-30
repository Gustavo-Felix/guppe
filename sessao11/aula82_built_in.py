"""
# Exemplo 01

import random as rdm

print(rdm.random())

from random import *

print(random())

import random

print(random.random())

from random import randint as rdi

print(rdi(5, 89 ))

from random import randint as rdi, random as rdm

print(rdi(5, 89 ))
print(rdm())
"""

from random import (
    random,
    randint,
    shuffle,
    choice
)

lista = ['Ge', 'ek']
shuffle(lista)

print(random())
print(randint(1, 10))
print(lista)
print(choice('Geek'))











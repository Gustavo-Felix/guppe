"""
tupla = (1, 2, 3)

print(tupla[1])

"""

from collections import namedtuple

# Forma 01 - Declaração namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 02

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 03

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade = 2, raca = 'chow-chow', nome = 'Ray')

print(ray)

# Acessando dados - Forma 01

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 02

print(ray.nome)
print(ray.idade)
print(ray.raca)





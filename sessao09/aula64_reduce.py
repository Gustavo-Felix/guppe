# Exemplo  01

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8]

mult = lambda x, y: x * y

res = reduce(mult, dados)

print(res)

res = 1

for n in dados:
    res = res * n

print(res)
"""
# Exemplo 01

nomes = ['Carlos', 'Camila', 'Cristina', 'Gustavo']

print(any(nome[0] == 'C' for nome in nomes))

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

from sys import getsizeof # Registra a quantidade de Bytes sendo usado

print(getsizeof('Geek'))

list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

gen_comp = getsizeof(x * 10 for x in range(1000))

print(list_comp)
print(set_comp)
print(dict_comp)
print(gen_comp)
"""

# Para finalizar

gen = (x * 10 for x in range(1000))

print(gen)
print(type(gen))

for num in gen:
    print(num)



















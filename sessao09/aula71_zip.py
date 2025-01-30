"""
# Exemplo 01

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(list(zip1))

zip1 = zip(lista1, lista2)

print(tuple(zip1))

zip1 = zip(lista1, lista2)

print(set(zip1))

zip1 = zip(lista1, lista2)

print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)

print(list(zip1))

tupla = (1, 2, 3, 4, 5)
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(lista, tupla, dicionario.values())

print(list(zt))

dados = [(0, 1), (2, 3), (4, 5)]

print(list(zip(*dados)))

"""

prova01 = [80, 91, 78]
prova02 = [98, 89, 53]

alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova01, prova02)}

print(final)







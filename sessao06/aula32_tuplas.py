"""
# Adição e Remoção de elementos na tupla não existem

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla1))

tupla3 = (4) # Não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # isso é uma tupla
print(tupla4)
print(type(tupla4))

# Tuplas são definidas pela virgula e nao pelos parenteses

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotando a tupla

tupla = 'Geek University', 'Python'

escola, curso = tupla

print(escola)
print(curso)

tupla = 1, 2, 3, 4, 5

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenar as tuplas

tupla1 = 1, 2, 3
print(tupla1)

tupla2 = 4, 5, 6
print(tupla2)

print(tupla1 + tupla2)

tupla1 += tupla2

print(tupla1)
print(tupla2)

# Ver se possui um tal elemento

tupla = 1, 2, 3
print(1 in tupla)

# Iterando uma tupla

tupla = 1, 2, 3

for i in tupla:
    print(i)

for ind, num in enumerate(tupla):
    print(ind, num)

# contando elementos em uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

"""

meses = ('janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses[5])

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

print(meses.index('Junho'))













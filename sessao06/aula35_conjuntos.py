"""
# Definindo um conjunto

# Forma 01

s = set({1, 2, 3, 4 ,5 ,5 ,6 ,7 ,8}) # Repare que temos valores repetidos

print(s)
print(type(s))

# o conjunto irá ignorar os valores repetidos

# Forma 02 - Mais Comum

s = {1, 2, 3, 4, 5, 5, 6, 7, 3}

print(s)
print(type(s))

if 3 in s:
    print(f'Tem o 3')
else:
    print('Não tem o 3')

dados = 99, 3, 3, 12, 3, 5, 98

# Listas aceitam valores duplicados

lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados

tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios NÃO aceitam valores duplicados

dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos NÃO aceitam valores duplicados

conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

s = {1, 'b', False, 34.5, 44}
print(s)
print(type(s))

for valor in s:
    print(valor)

# Usos interessantes

cidades = ['Belo Horizonte', 'São Paulo', 'Cuiaba', 'São Paulo', 'Campo Grande']

print(cidades)
print(len(cidades))

print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
print(s)

# Remover elementos

s = {1, 2, 3}

print(s)

# Forma 01

s.remove(3)

print(s)

# Forma 02

s.discard(2)

print(s)

# Copiar Elementos

s = {1, 2, 3}

print(s)

# Forma 01 - deep copy

novo = s.copy()

print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 02 - Shallow copy

novo = s
novo.add(4)
print(novo)
print(s)

# Remover todos os elementos de um conjunto

s.clear()
print(s)

# Métodos Matemáticos

estudantes_python = {'Marcos', 'Helen', 'Patricia', 'Pedro', 'Ana'}
estudantes_java = {'Fernando', 'Gustavo', 'Ana', 'Patricia'}

# Precisamos Gerar um conjunto com estudantes unicos

# Forma 01 - Union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 02 - pipe

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Estudantes Estao nos dois cursos

# Forma 01 - intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Froma 02 - &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Estudantes que esta em um so curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(min(s))
print(max(s))
print(len(s))










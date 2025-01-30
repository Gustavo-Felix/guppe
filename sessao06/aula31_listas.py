"""
# Exemplo 01 - Checar Determinado Valor em uma lista, ARRAY.

print('Exemplo 01:')
print('')

num = 2

if num in lista1:
    print('Numero encontrado!')
else:
    print('Numero nao encontrado')

# Exemplo 02 - Ordenando a Lista com sort

print('')
print('Exemplo 02:')
print('')

lista1.sort()
print(lista1)

# Exemplo 03 - Contagem do mesmo item em uma lista

print('')
print('Exemplo 03:')
print('')

print(lista1.count(1))
print(lista5.count('e'))

# Exemplo 04 - Atribuindo elementos na lista - OBS: Apenas UM dado por vez

print('')
print('Exemplo 04:')
print('')

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Possui [8, 3, 1]')

# Atribuir os VALORES e Não uma LISTA na lista - .extends

lista1.extend([22, 34, 63, 90])
print(f'{lista1} - Adicionou apenas os numeros e nao a lista na lista igual realizado a cima')

# Exemplo 05 - Inserir o valor na posição que a pessoa quiser - Não Substitui o valor 'original'

lista1.insert(2, 'Novo Valor na posição 3')
print(lista1)

# Exemplo 06 - Pode juntar duas linhas

# lista1 += lista2
# lista1.extend(lista2)
print(lista1)

# Exemplo 07 - Inverter as Listas

# Forma 01
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Forma 02

lista1.reverse()
lista2.reverse()

print(lista1[::-1])
print(lista2[::-1])

# Exemplo 08 - Copiar as Listas

lista6 = lista2.copy()

print(lista6)

# Exemplo 9 - Contar os elementos

print(len(lista2))

# Exemplo 10 - Remove o ultimo elemento - Retorna o elemento

print(lista1)
lista1.pop()
print(lista1)

# Exemplo 11 - Remover Todos os elementos

print(lista5)
lista5.clear()
print(lista5)

# Exemplo 12 - Podemos repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Exemplo 13 - podemos converter uma string para lista

# Forma 01 - split separa por espaço entre elas, por padrão

curso = "Python Geek University"
print(curso)
curso = curso.split()
print(curso)

# Forma 02 -

curso = "Curso,Python,em,essencial"
print(curso)
curso = curso.split(',')
print(curso)

# Exemplo 14 - Converter lista para string

print(lista6)

curso = ' '.join(lista6)

print(curso)

# Exemplo 15 - iterando listas

# Forma 01 - Utilizando FOR

for elemento in lista6:
    print(elemento)

# Forma 02 - Utilizando WHILE

carrinho = []
produto = ''
while produto != 'sair':
    print(f'Digite um produto ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Exemplo 16 - Utilizando variaveis em listas

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]

print(numeros)

# Exemplo 17 - acessando elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

# Forma 01 - Sequencia

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Forma 02 - Reverso

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])


for cor in cores:
    print(cor)

ind = 0
while ind < len(cores):
    print(cores[ind])
    ind += 1

cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar indice em um for

for ind, cor in enumerate(cores):
    print(ind, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(33)
lista.append(32)
lista.append(33)
print(lista)

# Encontrar indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 3 ,13]

print(numeros.index(6))

print(numeros.index(9))

# Se nao tiver o valor na lista, vai dar erro
# print(numeros.index(19))

print(numeros.index(5))

print(numeros.index(5, 1))

print(numeros.index(5, 1, 5))

type([])

lista1 = [1, 99, 90, 77, 2, 1]

lista2 = ['G', 'e', 'e', 'k', ' ','U']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos atribuir qualquer tipo de dado, inclusive misturar
lista6 = [1, 'Python', 1.12, True]

# SLICING

# lista[inicio:fim:passo]

lista = [1, 2, 3, 4, 5, 6, 7, 8]

print(lista[::])
print(lista[1::])
print(lista[:2:])
print(lista[1::2])
print(lista[3:1:-1])

nome = ['Geek', 'University']

nome[0], nome[1] = nome[1], nome[0]

print(nome)

nome.reverse()

print(nome)

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # Soma
print(max(lista)) # Valor maximo
print(min(lista)) # Valor minimo
print(len(lista)) # Tamanho

# Transformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de lista

lista1 = [1, 2, 3]

num1, num2, num3 = lista1

print(num1)
print(num2)
print(num3)
"""

# Copiando uma lista para outra - shallow copy    e    deep copy

# Forma 01 - Duas Listas Diferente - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Forma 02 - Modificar a lista original e a outra lista ao mesmo tempo - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)

nova.append(4)

print(lista)
print(nova)









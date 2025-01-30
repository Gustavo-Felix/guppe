"""
# Exemplo 01

import statistics

dados = [1.2, 2.3, 1.3, 9.4, 4.4, -0.1]

media = statistics.mean(dados)

print(media)

res = filter(lambda x: x > media, dados)

print(list(res))

print(f'Novamente: {list(res)}')

# OBS: Essa função se auto-destroi após o primeiro uso, igualmente a Função map

paises = [' ', 'Argentina', ' ', 'Brazil']

print(paises)

res = filter(lambda x: len(x.strip()) > 0, paises)

print(list(res))

# res = filter(None, paises)
# print(list(res))


usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu amo bolos', 'Eu amo pães', 'Amo pizza']},
    {'username': 'Gustavo', 'tweets': ['Amo pizza']},
    {'username': 'Pedro', 'tweets': []},
    {'username': 'Matheus', 'tweets': ['Eu amo bolos', 'Eu amo pães']},
    {'username': 'Richard', 'tweets': []},
    {'username': 'Maria', 'tweets': []}
]

# Forma 01
res1 = list(filter(lambda usuario: usuario['tweets'] == [],usuarios))

# Forma 02
res2 = list(filter(lambda usuario: len(usuario['tweets']) == 0,usuarios))

# Forma 03
res3 = list(filter(lambda usuario: not usuario['tweets'],usuarios))


print(res1)
print(res2)
print(res3)
"""

# Combinar Filter e Map

nomes = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5,nomes)))

print(lista)















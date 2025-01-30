"""
# Exemplo 01

numeros = [1, 4, 7, 2, 3]

print(numeros)
print(sorted(numeros)) # Retorna os valor em ordem em LISTA
print(numeros)

numeros = [1, 4, 7, 2, 3]

print(sorted(numeros))

print(sorted(numeros, reverse=True))

print(numeros)


usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu amo bolos', 'Eu amo pães', 'Amo pizza']},
    {'username': 'Gustavo', 'tweets': ['Amo pizza']},
    {'username': 'Pedro', 'tweets': [], 'Cor': 'Amarelo'},
    {'username': 'Matheus', 'tweets': ['Eu amo bolos', 'Eu amo pães']},
    {'username': 'Richard', 'tweets': []},
    {'username': 'Maria', 'tweets': [], 'musica': 'Rook'}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario['username'])) # Ordena em ordem Alfabetica

print(sorted(usuarios, key=lambda usuario: usuario['tweets']))
"""

musicas = [
    {'Titulo': 'ei mo', 'Tocou': 3},
    {'Titulo': 'ei mo', 'Tocou': 32},
    {'Titulo': 'ei mo', 'Tocou': 64},
    {'Titulo': 'ei mo', 'Tocou': 87}
]

print(sorted(musicas, key=lambda musica: musica['Tocou']))

print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))
















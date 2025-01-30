"""
# Exemplo 01 - max()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Tupla

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}# Dicionario

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

print(max(lista))
print(max(tupla))
print(max(conjunto))
print(max(dicionario.values()))

# Exemplo 02 - min()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Tupla

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}# Dicionario

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}

print(min(lista))
print(min(tupla))
print(min(conjunto))
print(min(dicionario.values()))

# Outros Exemplos

nomes = ['Ana', 'Sansom', 'Thais']

print(min(nomes))
print(max(nomes))

print(max(nomes, key= lambda nome: len(nome)))

print(min(nomes, key= lambda nome: len(nome)))


"""

musicas = [
    {'Titulo': 'ei mo (Min)', 'Tocou': 3},
    {'Titulo': 'ei mo', 'Tocou': 32},
    {'Titulo': 'ei mo', 'Tocou': 64},
    {'Titulo': 'ei mo (max)', 'Tocou': 87}
]

#print(min(musicas, key=lambda musica: musica['Tocou'])['Titulo'])
#print(max(musicas, key=lambda musica: musica['Tocou'])['Titulo'])

max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['Titulo'])

min = 99999
for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['Titulo'])









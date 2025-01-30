"""
# Forma 01 - Mais comum

paises = {'br': 'brasil', 'eua':'estados unidos'}

print(paises)
print(type(paises))

# Forma 2 - Menos comum

paises1 = dict(br = 'Brasil', eua = 'Estados unidos')

print(paises1)

# Acessando elementos

# Forma 01

print(paises['br'])

# Forma 02

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru', 'Não Encontrei o pais')

if pais:
    print('Encontrei o pais')
else:
    print('Não Encontrei o pais')

print('br' in paises)
print('estados unidos' in paises)

localidades = {
    (35.2355, 39.6957): 'Escritório em Tokyo',
    (39.3255, 43.4235): 'Escritório em Nova York',
    (35.2355, 39.6957): 'Escritório em São Paulo'

}

print(localidades)

# Adicionar elementos em um dicionario

receita = {'jan': 200, 'fev': 360}

print(receita)

# Forma 01

receita['mar'] = 620

print(receita)

# Forma 02

novo_dado = {'maio': 400}

receita.update(novo_dado)

print(receita)

receita['maio'] = 200

print(receita)


# Remover dados em uma receita

receita = {'jan': 200, 'fev': 360, 'mar': 870}

print(receita)

ret = receita.pop('mar')
print(ret)

print(receita)

del receita['fev']

print(receita)

# Forma 01 - Lista

carrinho = []

produto1 = ['Playstation 4', 1, 4000.00]
produto2 = ['God of War', 3, 190.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Forma 02 - Tupla

produto1 = ('Playstation 4', 1, 4000.00)
produto2 = ('God of War', 3, 190.00)

carrinho = (produto1, produto2)

print(carrinho)

# Forma 03 - Dicionario

carrinho = []

produto1 = {'Nome':'Playstation 4', 'Quantidade': 5,'Preço': 4300.00}
produto2 = {'Nome':'God of War', 'Quantidade': 3,'Preço': 280.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Metodos do Dicionario

d = dict(a = 1, b = 2, c = 3)

print(d)

# Limpar Dados

d.clear()

print(d)

# Copiar de um dicionario para outro - Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(novo)
print(d)

# Shalow Copy

novo = d
print(novo)

novo['d'] = 4

print(novo)
print(d)
"""

precos = {
    'Carro': 9000,
    'Car': 1999
}

for item in precos:
    print(item)

















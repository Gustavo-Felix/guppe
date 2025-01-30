"""
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

print(receita.keys())


for chave in receita.keys():
    print(receita[chave])

print(receita.values())

for valor in receita.values():
    print(valor)

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e Valor = {valor}')

"""
receita = {'jan': 200, 'fev': 350, 'mar': 400}

print(receita)

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))



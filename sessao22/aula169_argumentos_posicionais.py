# Exemplo 01

# valor = '67.3'
# print(float(valor))

def comprimenta(nome, /):
    return f'Olá {nome}'

print(comprimenta('Gustavo'))
print(comprimenta(nome='Gustavo'))

def comprimenta2(*, nome):
    return f'Olá {nome}'

print(comprimenta2('Gustavo'))
print(comprimenta2(nome='Gustavo'))
"""
# Exemplo 01

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(3))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('GUSTAVO  ', 'fÉLIX'))

amar = lambda: 'como nao amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(2))
print(duas(7, 2))
print(tres(3, 6, 4))


# Exemplo 02

autores = ['Isaac Shie', 'Marcos tulio', 'Paulo Leda', 'Paulo sig Carlos']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""

def geradora_quadratica(a, b, c):
    """Retorna a Função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

# OU

print(geradora_quadratica(1, 2, 3)(5))







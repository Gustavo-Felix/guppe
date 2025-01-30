# Exemplo 01

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

print(list(res))
print(tuple(reversed(lista)))
print(set(reversed(lista))) # Não define ordem

for letra in reversed('Geek'):
    print(letra, end='')

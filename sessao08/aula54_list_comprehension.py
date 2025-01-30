"""
# Exemplo 01

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

numeros = [1, 2, 3, 4, 5]

def dobrar(num):
    return num * 2

res = [dobrar(num) for num in numeros]

print(res)

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

print([numero * 2 for numero in numeros])

amigos = ['maria', 'julia', 'guilherme']

print([amigo.title() for amigo in amigos])


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)













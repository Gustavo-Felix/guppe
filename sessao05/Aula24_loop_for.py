"""
# Exemplo 01
for letra in nome:
    print(letra)

# Exemplo 02
for numero in lista:
    print(numero)

# Exemplo 03
for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for valor in enumerate(nome):
    print(valor[0])

qtd = int(input("Quantas vezes esse loop deve rodar: "))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma += num
print(soma)
"""

nome = "Geek University"

for letra in nome:
    print(letra, end='')





"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
"""

lista = []
i = 0
a = 0

while i < 6:
    n = int(input('Digite um Valor:'))
    lista.append(n)
    i += 1

print(lista)

for a in lista:
    print(a)
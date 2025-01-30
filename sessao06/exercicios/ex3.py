"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""

lista = []
i = 0
p = 0
ip = 0

while i < 10:
    n = int(input('Digite um valor: '))
    lista.append(n)
    i += 1

for a in lista:
    if a % 2 == 0:
        print(f'O valor {a} é PAR!')
        p += 1
    else:
        print(f'O valor {a} é ÍMPAR')
        ip += 1

print('Números Pares: ', p)
print('Números Ímpares: ', ip)
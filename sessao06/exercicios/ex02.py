"""
2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.

"""

a = [1, 0, 5, -2, -5, 7]

soma = a[0] + a[1] + a[5]

print(f'A soma é {soma}')
print(' ')
print('Os números são:')

a[5] = 100

for i in a:
    print(i)

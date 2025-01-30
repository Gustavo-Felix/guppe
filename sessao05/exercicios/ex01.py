"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""

# Forma 01

num = int(input('Qual Número você gostaria de saber os multiplos? '))
mult = int(input('Quantos multiplos você gotaria de saber? '))

for i in range(0, (mult * num), num):
    print(i+num)

# Forma 02

num = 0
cont = 0

while cont < 5:
    num += 3
    print(num)
    cont +=1

# Forma 03

ind = 1
cont1 = 0

while cont1 < 5:
    if ind % 3 == 0:
        print(f'O Número {ind} é multiplo de 3!')
        cont1 += 1
    ind += 1
print("Fim!")
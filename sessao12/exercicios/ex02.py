"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
vogais e quantas são consoantes.
"""

vogais = 0
consoantes = 0

nome = str(input('Digite o Nome do arquivo que deseja indentificar: '))

with open(nome, 'r+') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        if linha.replace('\n', '').lower() in ['a', 'e' , 'i', 'o', 'u']:
            vogais += 1
        else:
            consoantes += 1


print(f'Vogais: {vogais}')
print(f'Consoantes: {consoantes}')



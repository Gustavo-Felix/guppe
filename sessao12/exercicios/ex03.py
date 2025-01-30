"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
arquivo possui.
"""

nome = str(input('Digite o Nome do arquivo que deseja indentificar: '))

with open(nome, 'r+') as arquivo:
    linhas = arquivo.readlines()
    print(len(linhas))



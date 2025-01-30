"""
1. Crie um programa que.
a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere
“0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""
with open('arq.txt', 'a') as arquivo:
    while True:
        n = input('Digite um caracter: ')
        if n != '0':
            arquivo.write(n)
            arquivo.write('\n')
        else:
            break

arquivo.close()

with open('arq.txt', 'r') as arquivo:
    print(arquivo.read())
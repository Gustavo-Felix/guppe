"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

lista = []
i = 0

def maior(lista):
    global i
    while i < 10:
        numero = int(input('Digite o número que deseja inserir na lista: '))
        i += 1
        lista.append(numero)
    print(max(lista))

maior(lista)
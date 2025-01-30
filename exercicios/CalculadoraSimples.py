import math
import os
import time

def limpa_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    return math.sqrt(x)

while True:
    limpa_terminal()
    print('(0) - Sair')
    print('(1) - Adição')
    print('(2) - Subtração')
    print('(3) - Multiplicação')
    print('(4) - Divisão')
    print('(5) - Potência')
    print('(6) - Raiz Quadrada')
    try:
        escolha = int(input('Digite a Opção que deseja realizar: '))
    except ValueError:
        print('É aceito apenas Números!')

    limpa_terminal()

    try:
        if escolha == 0:
            break
        if escolha == 1:
            x = int(input('Digite o Primeiro Número: '))
            y = int(input('Digite o Segundo Número: '))
            print('\n')
            print(f'O Resultado da Soma é {soma(x, y)}')
            time.sleep(5)
            limpa_terminal()
        if escolha == 2:
            x = int(input('Digite o Primeiro Número: '))
            y = int(input('Digite o Segundo Número: '))
            print('\n')
            print(f'O Resultado da Subtração é {subtracao(x, y)}')
            time.sleep(5)
            limpa_terminal()
        if escolha == 3:
            x = int(input('Digite o Primeiro Número: '))
            y = int(input('Digite o Segundo Número: '))
            print('\n')
            print(f'O Resultado da Multiplicação é {multiplicacao(x, y)}')
            time.sleep(5)
            limpa_terminal()
        if escolha == 4:
            x = int(input('Digite o Primeiro Número: '))
            y = int(input('Digite o Segundo Número: '))
            print('\n')
            print(f'O Resultado da Soma é {divisao(x, y)}')
            time.sleep(5)
            limpa_terminal()
        if escolha == 5:
            x = int(input('Digite o Número que Deseja ser para ser a base: '))
            y = int(input('Digite o Número para ser a potência: '))
            print('\n')
            print(f'O Resultado da Potência é {potencia(x, y)}')
            time.sleep(5)
            limpa_terminal()
        if escolha == 6:
            x = int(input('Digite o Número que Deseja saber a raiz quadrada: '))
            print('\n')
            print(f'O Resultado da Potência é {raiz_quadrada(x)}')
            time.sleep(5)
            limpa_terminal()
    except ValueError:
        print('É aceito apenas Números!')
        limpa_terminal()





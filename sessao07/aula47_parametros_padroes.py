"""
# Existem funções opcionais e obrigatórias

def exponencial(num, potencia = 2):
    return num ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(5)) # Por padrão eleve ao quadrado


def mostra_informacao(nome = 'Gustavo', instrutor = False):
    if nome == 'Gustavo' and instrutor:
        print(f'Bem-vindo, instrutor {nome}')
    elif nome == 'Gustavo':
        print(f'Bem-vindo {nome}')
    elif instrutor:
        print(f'Bem-vindo Instrutor!')
    else:
        print(f'Bem-vindo')

mostra_informacao('Nome', True)

def soma(a, b):
    return a + b

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Variaveis Globais
# Variaveis Locais

instrutor = 'geek' # Global

def diz_oi():
    instrutor = 'Python' # Local
    return f'Oi {instrutor}'

print(diz_oi())

"""

total = 0

def incrementa():
    global total

    total += 1
    return total

print(incrementa())















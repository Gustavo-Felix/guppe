"""
# Exemplo 01

try:
    geek()
except:
    print('Deu erro')

# Exemplo 02 - Erro Especifico - NameError

try:
    len(1)
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 03 - Erro Especifico - TypeError

try:
    len(1)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 04 - Erro Especifico

try:
    len(1)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Exemplo 05 - Erro Especifico

try:
    print('geek'[10])
except NameError as err1:
    print(f'NameError: {err1}')
except TypeError as err2:
    print(f'TypeError: {err2}')
except SyntaxError as err3:
    print(f'SyntaxError: {err3}')
except:
    print('Deu um Erro diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'Nome': 'Geek'}

print(pega_valor(dic, 'Nome'))











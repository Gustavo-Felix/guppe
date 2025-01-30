"""
# Exemplo 01 - com Pycharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um Problema: {err}'

print(dividir(4, 0))


# Exemplo 02 - com Python Debugger

# Comandos do pdb
# l - listar
# n - Proxima linha
# p - imprime a variavel
# c - Continua a execução

import pdb

nome = 'Gustavo'
sobrenome = 'Felix'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' Faz ' + curso

print(final)

# Exemplo 03 - com Python Debugger

# Comandos do pdb
# l - listar
# n - Proxima linha
# p - imprime a variavel
# c - Continua a execução

nome = 'Gustavo'
sobrenome = 'Felix'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' Faz ' + curso

print(final)

"""

# Exemplo 03 - com Python Debugger

# Comandos do pdb
# l - listar
# n - Proxima linha
# p - imprime a variavel
# c - Continua a execução

nome = 'Gustavo'
sobrenome = 'Felix'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' Faz ' + curso

print(final)




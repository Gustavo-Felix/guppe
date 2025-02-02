"""
# Exemplo 01 - Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma Função (Logar) dentro de outra
        print(f'Voce Está chamando {funcao.__name__}')
        print(f'Aqui a Documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(x, y):
    # Soma Dois números.
    return x + y

# print(soma(10, 30))

print(soma.__doc__)
"""

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma Função (Logar) dentro de outra"""
        print(f'Voce Está chamando {funcao.__name__}')
        print(f'Aqui a Documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(x, y):
    """Soma Dois números."""
    return x + y

# print(soma(10, 30))
print(soma.__name__)
print(soma.__doc__)
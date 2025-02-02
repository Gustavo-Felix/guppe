"""
# Exemplo 01

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou a/o {nome}'

print(saudacao('Gustavo'))

def gritar(funcao):
    def aumento(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumento

@gritar
def saudacao(nome):
    return f'Eu sou o {nome}'

@gritar
def ordenar(principal, acompanhado):
    return f'Olá, eu gotaria de {principal} acompanhado de {acompanhado}'

print(saudacao('Gustavo'))
print(ordenar('Picanha', 'Batata Frita'))

"""

def verifica(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'O valor inserido tem que ser igual ao {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica('Pizza')
def comida(*args):
    print(args)

@verifica(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))








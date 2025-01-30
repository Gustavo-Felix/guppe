"""
# Exemplo 01

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='amarelo', julia='azul', joao='vermelho')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['Geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'Geek' in kwargs:
        return f'{kwargs['Geek']} Geek!'
    else:
        return 'Não te reconheço!'

print(cumprimento_especial())
print(cumprimento_especial(Geek='Python'))
print(cumprimento_especial(Geek='Oi'))
print(cumprimento_especial(Geek='especial'))

def minha_funcao(idade, nome, *args, solteiro = False, **kwargs):
    print(f'{nome} tem {idade} anos de idade!')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    print('')

minha_funcao(18, 'julia')
minha_funcao(29, 'João', 4, 5, 6, True)
minha_funcao(37, 'Mario', eu = 'vai', voce = 'fica')
minha_funcao(27, 'Julio', 9, 7, 4, java=False, python=True)

# Ordem correta dos parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='Félix', cargo='Aluno'))


# Forma incorreta
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='Félix', cargo='Aluno'))

# Desempacotar com o kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes = {'nome': 'Gustavo', 'sobrenome':'Félix'}

print(mostra_nomes(**nomes))
"""

def soma_numeros(a, b, c, **kwargs):
    print(a + b + c, kwargs)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3, nome = 'Geek')

soma_numeros(**dicionario)

soma_numeros(**dicionario, lang='Python')















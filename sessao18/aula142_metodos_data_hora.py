"""
# Exemplo 01

import datetime

agora = datetime.datetime.now() # Pode especificar o fuso-horario
print(type(agora))
print(repr(agora))
print(agora)

hoje = datetime.datetime.today()
print(type(hoje))
print(repr(hoje))
print(hoje)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(type(manutencao))
print(repr(manutencao))
print(manutencao)


manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday()) # Dias da semana em weekday, comecam em 0. 0 = Segunda-feira (monday)

import datetime

aniversario = input('Digite a data do seu aniversário (dd/mm/yyyy): ')
aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print(f'Você nasceu em uma Segunda-feira')
elif aniversario.weekday() == 1:
    print(f'Você nasceu em uma Terça-feira')
elif aniversario.weekday() == 2:
    print(f'Você nasceu em uma Quarta-feira')
elif aniversario.weekday() == 3:
    print(f'Você nasceu em uma Quinta-feira')
elif aniversario.weekday() == 4:
    print(f'Você nasceu em uma Sexta-feira')
elif aniversario.weekday() == 5:
    print(f'Você nasceu em uma Sábado')
elif aniversario.weekday() == 6:
    print(f'Você nasceu em uma Domingo')

def formata_data(data):
    if data.month == 1:
        print(f'{data.day} de Janeiro de {data.year}')
    if data.month == 2:
        print(f'{data.day} de Fevereiro de {data.year}')
    if data.month == 3:
        print(f'{data.day} de Março de {data.year}')
    if data.month == 4:
        print(f'{data.day} de Abril de {data.year}')
    if data.month == 5:
        print(f'{data.day} de Maio de {data.year}')
    if data.month == 6:
        print(f'{data.day} de Junho de {data.year}')
    if data.month == 7:
        print(f'{data.day} de Julho de {data.year}')
    if data.month == 8:
        print(f'{data.day} de Agosto de {data.year}')
    if data.month == 9:
        print(f'{data.day} de Setembro de {data.year}')
    if data.month == 10:
        print(f'{data.day} de Outubro de {data.year}')
    if data.month == 11:
        print(f'{data.day} de Novembro de {data.year}')
    if data.month == 12:
        print(f'{data.day} de Dezembro de {data.year}')


import datetime
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='en', target='pt')

def formata_data(data):
    return f"{data.day} de {tradutor.translate(data.strftime('%B'))} de {data.year}"

hoje = datetime.datetime.today()
hoje_formatado = hoje.strftime('%d/%m/%Y')

print(formata_data(hoje))

nascimento = datetime.datetime.strptime('26/07/2007', '%d/%m/%Y')

print(nascimento)

nascimento = input('Digite a data do seu nascimento (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

almoco = datetime.time(12, 30, 00)

print(almoco)

# Loop for
marcando_tempo = timeit.timeit('"-" .join(str(n) for n in range(100))', number=10000)
print(marcando_tempo)

# list Comphesion
marcando_tempo = timeit.timeit('"-" .join([str(n) for n in range(100)])', number=10000)
print(marcando_tempo)

# map

marcando_tempo = timeit.timeit('"-" .join(map(str, range(100)))', number=10000)
print(marcando_tempo)
"""

import datetime
import timeit
import functools

def test(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(test, 2), number=10000))

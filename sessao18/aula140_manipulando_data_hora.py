"""
# Exemplo 01

import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.datetime.now()) # 2025-02-08 11:05:37.126424

print(repr(datetime.datetime.now())) # datetime.datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, MICROSECOND)

inicio = datetime.datetime.now()

print(inicio)

inicio = inicio.replace(year=2023, hour=11, minute=0, second=0, microsecond=0)

print(inicio)

print(type(evento))
print(evento)

aniversario = str(input('Digite seu aniversario (dd/mm/yyyy): '))

aniversario = aniversario.split('/')

aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))

print(aniversario)

"""

import datetime

evento = datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

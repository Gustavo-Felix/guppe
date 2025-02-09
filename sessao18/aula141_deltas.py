# Exemplo 01

import datetime

hoje = datetime.datetime.now()
aniversario = datetime.datetime(2025, 7, 26)

tempo = aniversario - hoje

print(repr(tempo))
print(type(tempo))
print(tempo)


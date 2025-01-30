"""
dicionario = {'Curso':'Python'}

print(dicionario)

print(dicionario['Curso'])

print(dicionario['outro'])

"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Python'

print(dicionario)

print(dicionario['outro'])

print(dicionario)
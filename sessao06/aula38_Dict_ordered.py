"""
dicionario = {'a': 1, 'b': 2}

for chave, valor in dicionario.items():
    print(f'A chave {chave}: valor {valor}')

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2})

for chave, valor in dicionario.items():
    print(f'chave = {chave}, Valor = {valor}')

"""
from collections import OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)



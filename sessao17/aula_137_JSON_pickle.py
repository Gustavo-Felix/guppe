"""
# Exemplo 01 - JSON

import json

ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)

import json

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

felix = Gato('Felix', 'Vira-lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)

# Escrevendo JSON com Pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

felix = Gato('Felix', 'Vira-lata')

# ret = jsonpickle.encode(felix)
# print(ret)

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""

# Lendo JSON com Pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

felix = Gato('Felix', 'Vira-lata')

# ret = jsonpickle.encode(felix)
# print(ret)

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(type(ret))
    print('')
    print(ret.nome)
    print(ret.raca)
    print('')
    print(ret)
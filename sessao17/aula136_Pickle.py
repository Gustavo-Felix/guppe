# Exemplo 01 - Pickle - Não é seguro contra dados maliciosos, NÃO UTILIZE PICKLE EM DADOS EXTERNOS

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')



felix = Gato('Felix')
duke = Cachorro('Duke')

# Escrita de arquivos Pickle

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, duke), arquivo)

# Leitura de arquivo Pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato se chama: {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é: {type(gato)}')
    print('')
    print(f'O cachorro se chama: {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é: {type(cachorro)}')
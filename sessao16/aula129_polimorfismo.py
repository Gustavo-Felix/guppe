# Exemplo 01

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método.')

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está latindo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está miando...')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está ratiando...')


# Teste

felix = Gato('Felix')
felix.falar()
felix.comer()

pluto = Cachorro('Pluto')
pluto.falar()
pluto.comer()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
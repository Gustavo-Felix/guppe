# Exemplo 01

class Gato:

    def __init__(self, nome):
        self.__nome= nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def miar(self):
        print(f'{self.nome} está miando...')

felix = Gato('Felix')
felix.miar()
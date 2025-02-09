"""

# Exemplo 01 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 02 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Teste

baleia = Aquatico('Wally')
print(baleia.cumprimento())
print(baleia.nadar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimento())

tux = Pinguim('Tux')
print(tux.cumprimento())
print(tux.andar())
print(tux.nadar())

print('')

print(f'Tux é Instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é Instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é Instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é Instância de object? {isinstance(tux, object)}')
print(f'Tux é Instância de Animal? {isinstance(tux, Animal)}')


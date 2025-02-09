"""
# Exemplo 01

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Salde de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta):
        self.__saldo -= valor
        conta.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

c1 = Conta('Gustavo', 500, 1000)
c2 = Conta('Bruna', 1000, 2000)

print(c1.extrato())
print(c2.extrato())
saldo_total = c1.get_saldo() + c2.get_saldo()
print(saldo_total)

"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Salde de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta):
        self.__saldo -= valor
        conta.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

c1 = Conta('Gustavo', 500, 1000)
c2 = Conta('Bruna', 1000, 2000)

print(c1.extrato())
print(c2.extrato())

saldo_total = c1.saldo + c2.saldo

print(saldo_total)

print(c1.__dict__)
c1.limite = 10000000
print(c1.__dict__)

print(c1.valor_total)
print(c2.valor_total)

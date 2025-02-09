"""
# Exemplo 01

lamp1 = Lampada('Azul', '110', '60') # Intância / Objeto
lamp1.ligar_desligar()
print(lamp1.checa_lampada())

cc1 = ContaCorrente('5000', '2000')

user = Usuario('Gustavo', 'Felix', 'gustavofelix@gmail.com', '123456')
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O Cliente {self.__nome} Diz "Oi"')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O Cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


clie1 = Cliente('Gustavo', '1111111111')
cc = ContaCorrente('5000', '10000', clie1)
cc.mostra_cliente()
clie1.diz()
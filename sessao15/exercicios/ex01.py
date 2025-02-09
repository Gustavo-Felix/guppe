"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

"""
from calendar import month
from datetime import date
class Pessoa:
    def __init__(self, nome: str, datanasc: date, email: str):
        self.__nome: str = nome
        self.__datanasc: date = datanasc
        self.__email: str = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__datanasc

    @data_nascimento.setter
    def data_nascimento(self, datanasc: date):
        self.__datanasc = datanasc

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    def imprimir(self):
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}')
        print(f'E-mail: {self.email}')

if __name__ == '__main__':
    p1 = Pessoa('Gustavo', date(2007, 7, 26), 'gustavo@gmail.com')
    p1.imprimir()



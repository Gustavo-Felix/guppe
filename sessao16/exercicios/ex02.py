"""
2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.
"""
from sessao16.exercicios.ex01 import Veiculo


class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas

    def imprimir(self):
        super().imprimir()
        print(f'Portas: {self.portas}')

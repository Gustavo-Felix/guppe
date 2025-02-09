"""
3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
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

marca = str(input('Digite a Marca do seu carro: '))
modelo = str(input('Digite o modelo do seu carro: '))
portas = int(input('Digite a quantidade de portas no seu carro: '))

carro1 = Carro(marca, modelo, portas)
carro1.imprimir()
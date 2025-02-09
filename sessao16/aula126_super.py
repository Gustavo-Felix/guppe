# Exempolo 01
from pydoc import classify_class_attrs


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        return f'Este animal faz esse som: {som}'

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca
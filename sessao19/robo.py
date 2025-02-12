class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar_bateria(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'Meu nome é {self.__nome.upper()}'
        return f'Bateria está {self.__bateria}%, por favor recarregue-a.'

    def aprender_habilidade(self, nova_hab, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_hab)
            return f'Aprendi {nova_hab.upper()}'
        elif custo > self.__bateria:
            return f'Bateria está {self.__bateria}%, por favor recarregue-a.'

from random import randint

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor

        self.__operacao: int = randint(1, 3)
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self: object, dificuldade: int) -> int:
        self.__dificuldade = dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op: str = 'Somar'
        elif self.operacao == 2:
            op: str = 'Subtrair'
        elif self.operacao == 3:
            op: str = 'Multiplicação'
        else:
            op: str = 'Desconhecida'
        return f'Valor1: {self.valor1}\nValor2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {self.operacao}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 100)
        elif self.dificuldade == 2:
            return randint(0, 1000)
        elif self.dificuldade == 3:
            return randint(0, 10000)
        elif self.dificuldade == 4:
            return randint(0, 1000000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta Correta!')
            certo = True
        else:
            print('Resposta Incorreta!')

        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ')
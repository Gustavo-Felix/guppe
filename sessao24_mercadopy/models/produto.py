from sessao24_mercadopy.utils.helper import formeta_float_str_moeda

class Produto:

    contador: int = 1

    def __init__(self: object, nome: str, preco: float):
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self: object) -> str:
        return f'Código: {self.__codigo} \nNome: {self.__nome} \nPreço: {formeta_float_str_moeda(self.__preco)}'
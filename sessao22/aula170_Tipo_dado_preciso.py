# Exemplo 01 - Literal Type

from typing import Literal

# def pegar_status(usuario: str) -> Literal['Conectado', 'Desconectado']:
#    pass

# def calcula(operacao: Literal['+', '-'], num: int, num2: int) -> None:
#     if operacao == '+':
#         print(num + num2)
#     elif operacao == '-':
#         print(num - num2)
#     else:
#         raise ValueError(f'Operação Inválida {operacao!r}')
#
# calcula('+', 2, 4)
# calcula('-', 2, 4)
# calcula('*', 2, 4)

# Exemplo 02 - Union
# from typing import Union
#
# def soma(num1: int, num2: int) -> Union[str, int]:
#     resultado: int = num1 + num2
#     if resultado > 50:
#         return f'O valor {resultado} é muito grande!'
#     else:
#         return resultado


# Exemplo 01

"""
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    aula147_doctests
1 items passed all tests:
   1 tests in aula147_doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

Trying:
    soma(4, 6)
Expecting:
    10
ok
1 items had no tests:
    aula147_doctests
1 items passed all tests:
   2 tests in aula147_doctests.soma
2 tests in 2 items.
2 passed and 0 failed.
Test passed.


def soma(a, b):
    #Soma dos números a e b
    #>>> soma(1, 2)
    #3

    #>>> soma(4, 6)
    #10
    return a + b

# print(soma(3, 4))

# Exemplo 02 - Aplicando o TDD

def duplicar_valores(valores):
    Duplica os valores em uma lista

    # >>> duplicar_valores([1, 2, 3, 4])
    [2, 4, 6, 8]
    # >>> duplicar_valores([])
    []
    # >>> duplicar_valores(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']
    # >>> duplicar_valores([True, None])
    Traceback (most recente call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    return [2 * elemento for elemento in valores]

def fala_oi():

    Fala oi

    #>>> fala_oi()
    'oi'

    return "oi"
"""




















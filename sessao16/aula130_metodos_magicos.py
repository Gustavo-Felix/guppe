"""
# Exemplo 01 - Métodos que utilizam dunder ( __metodo__ ) - Existe Preferência nos metodos dunders

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return self.__titulo
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto foi deletado da mémoria!')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += str(self) + ' '
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python', 'Gustavo', 200)
livro2 = Livro('IA', 'Bruna', 350)

print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))
print(livro1 + livro2)
print(livro1 * 100)
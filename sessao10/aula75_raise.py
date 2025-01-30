"""
# Exemplo 01

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O Texto Precisa Ser uma String!')
    if type(cor) is not str:
        raise TypeError('A Cor Precisa Ser uma String!')
    print(f'O texto {texto} Será impresso na cor {cor}')

colore('Geek', True)

"""

def colore(texto, cor):
    cores = ('Verde', 'Amarelo', 'Branco', 'Azul')
    if type(texto) is not str:
        raise TypeError('O Texto Precisa Ser uma String!')
    if type(cor) is not str:
        raise TypeError('A Cor Precisa Ser uma String!')
    if cor not in cores:
        raise ValueError(f'A Cor precisa ser uma entre {cores}')
    print(f'O texto {texto} Será impresso na cor {cor}')

colore('Geek', 'Branco')





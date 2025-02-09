# Exemplo 01

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos!'
    return a + b

res1 = soma_numeros_positivos(2, 2)
# res2 = soma_numeros_positivos(-2, 2) # AssertionError
print(res1)
# print(res2)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'lanche',
        'sorvete',
        'Cachorro quente'
    ], 'A Comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

print(comer_fast_food('pizza'))
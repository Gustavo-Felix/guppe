# Exemplo 01 - Generator function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(5)

# for n in gen:
#     print(n)

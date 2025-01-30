"""
# Exemplo 01

listas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] # Matriz 3 X 3

print(listas)
print(type(listas))


print(listas[0][2])
print(listas[1][2])
print(listas[2][-2])


# Iterando com loops

for lista in listas:
    for num in lista:
        print(num)



# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
"""

# Outros Exemplos

# Gerar uma Matrix 3 X 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

jogo_velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]

print(jogo_velha)










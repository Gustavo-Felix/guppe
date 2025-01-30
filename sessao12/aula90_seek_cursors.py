"""
# Exemplo 01

arquivo = open('texto.txt')

print(arquivo.read())
print(arquivo.read())

# Movimentando o cursor com seek() - movimenta de caracter para caracter

arquivo.seek(0)
print(arquivo.read())

# Exemplo - readline()

arquivo = open('texto.txt')

print(arquivo.readline())
print(arquivo.readline())

# Exemplo - readlines()

linhas = arquivo.readlines()

print(len(linhas))

"""

"""
# 1 - Abriu o arquivo
arquivo = open('texto.txt')

# 2 - Usar o arquivo
print(arquivo.read())
print(arquivo.closed) # Se o arquivo está fechado ou não - bool

# 3 - Fechar
arquivo.close()

print(arquivo.closed) # Se o arquivo está fechado ou não - bool
"""

# Exemplo 01

arquivo = open('texto.txt')

print(arquivo.read())
print(arquivo.read())

# Movimentando o cursor com seek() - movimenta de caracter para caracter

arquivo.seek(3)
print(arquivo.read())
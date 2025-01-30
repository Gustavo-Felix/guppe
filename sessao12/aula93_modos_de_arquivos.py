"""
r - Ler o arquivo
w - Escreve o arquivo
x - abre para escrita, somente se o arquivo não existir
a - Adiciona conteúdo ao final do arquivo
+ - Leitura e escrita - Temos controle do cursor


# Exemplo 01 - x

try:
    with open('richard_gay.txt', 'x') as arquivo:
        arquivo.write('Olá!')
except FileExistsError:
    print('Arquivo já existe!')

# Exemplo 02 - a

with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Digite uma fruta, ou sair, para Sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# Exemplo 03 - +

with open('richard_gay.txt', 'r+') as arquivo1:
    arquivo1.write('Tesstee!')

"""




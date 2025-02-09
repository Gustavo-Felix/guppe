"""
# Exemplo 01 - Forma Não Recomendável

with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

# Exemplo 02 - Reader

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pula o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} Nasceu no(a) {linha[1]} e mede {linha[2]}')

# Exemplo 03 - DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} Nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")
"""

# Exemplo 03 - DictReader - Com outro separador

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f"{linha['Nome']} Nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")
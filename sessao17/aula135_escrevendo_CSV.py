"""
# Exemplo 01 - writerow() - Escreve uma linha

from csv import writer

horas = 0

with open('filmes.csv', 'a', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'Sair':
        filme = str(input('Digite o Nome do filme: ')).title()
        if filme != 'Sair':
            genero = str(input('Digite o gênero do filme: ')).title()
            duracao = int(input('Digite a duração do filme (em minutos): '))
            while duracao > 59:
                horas = horas + 1
                duracao = duracao - 60
            if duracao < 10:
                duracao = f'0{duracao}'
            duracao = f'{horas}:{duracao}Hora(s)'
            escritor_csv.writerow([filme, genero, duracao])

"""

# Exemplo 02 - dictwriter

from csv import DictWriter

horas = 0

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'Sair':
        filme = str(input('Digite o Nome do filme: ')).title()
        if filme != 'Sair':
            genero = str(input('Digite o gênero do filme: ')).title()
            duracao = int(input('Digite a duração do filme (em minutos): '))
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 2024”
"""


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def data_por_extenso(data):
    dia = data[0]
    mes = int(data[1])
    ano = data[2]

    print(f'{dia} de {meses[mes-1]} de {ano}')

Data = input('Digite a Data que gostaria de fazer por extenso: ')

dividido = Data.split('/')
print(dividido)
# ['01', '01', '2024']
data_por_extenso(dividido)


"""
meses = {0:'Janeiro', 1:'Fevereiro', 2:'Março', 3:'Abril', 4:'Maio', 5:'Junho', 6:'Julho', 7:'Agosto', 8:'Setembro', 9:'Outubro', 10:'Novembro', 11:'Dezembro'}

def data_por_extenso(data):
    dia = data[0]
    mes = int(data[1])
    ano = data[2]
    print(f'{dia} de {meses[mes - 1]} de {ano}')


Data = input('Digite a Data que gostaria de fazer por extenso: ')

dividido = Data.split('/')

#print(dividido)

data_por_extenso(dividido)
"""

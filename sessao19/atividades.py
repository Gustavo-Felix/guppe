def comer(comida, saudavel):
    if saudavel == True:
        final = 'me mantem em forma.'
    else:
        final = 'só se vive uma vez.'

    return f'Estou comendo {comida} por que {final}'

def dormir(horas):
    if horas > 8:
        return 'Descansei muito bem.'
    else:
        return 'Continuo Cansado.'

def engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False

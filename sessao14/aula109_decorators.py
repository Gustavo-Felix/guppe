"""
# Exemplo 01 - Não Recomendavel

def seja_educado(funcao):
    def sendo():
        print('Foi um Prazer te conhecer')
        funcao()
        print('Tenha um Ótimo dia')
    return sendo

def saudacao():
    print('Seja Bem-vinda')

teste = seja_educado(saudacao)
teste()

# Exemplo 02 - Recomendavel

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Olá, Tudo Bem?')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro!')

apresentando()
"""


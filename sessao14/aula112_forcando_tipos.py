# Exemplo 01

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):   # resulta em (msg, vezes) - (str, int) = (msg, str) - (vezes, int)
                novo_args.append(tipo(valor))
            return funcao(*args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)


repete_mensagem('a', '3') # Transforma o msg em string     e      vezes em int  utilizando o zip()

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir(1, 3)
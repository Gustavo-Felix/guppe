from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Digite o nível de dificuldade desejada ( 1 | 2 | 3 | 4): '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado desta operação: ')
    calc.mostrar_operacao()
    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos(s)')

    continuar: str = str(input('Deseja continuar no jogo? '))

    if continuar.title() == 'Sim':
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} pontos!')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
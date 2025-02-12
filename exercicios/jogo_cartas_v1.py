import random
from typing import List, Tuple, Dict

naipes: List[str] = '♦️ ♠️ ♥️ ♣️'.split()
cartas: List[str] = '2 3 4 5 6 7 8 9 10 Q J K A'.split()

Carta = Tuple[str, str]
Baralho = List[Carta]

def criar_baralho(aleatorio: bool = False) -> Baralho:
    """Cria um baralho"""
    baralho: Baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: Baralho) -> Tuple[Baralho, Baralho, Baralho, Baralho]:
    """Gerencia a mão de cartas de acordo com o baralho"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar() -> None:
    """inicia um jogo de cartas para 4 jogadores"""
    cartas: Baralho = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, Baralho] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
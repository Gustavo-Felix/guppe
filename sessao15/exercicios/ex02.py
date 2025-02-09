"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

"""
from datetime import date
from ex01 import Pessoa


class Agenda:

    def __init__(self):
        """
        Inicia com um parâmetro 'self.__contatos' sendo uma Lista da Classe (Pessoa) vazia
        """
        self.__contatos: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos

    def armazenar_contato(self, contato: Pessoa) -> None:
        self.contatos.append(contato)

    def remover_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)

    def buscar_contato(self, nome: str) -> None:
        for i, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O Contato {nome} está na posição {i}')

    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()


if __name__ == '__main__':

    contato1: Pessoa = Pessoa('Gustavo', date(2007, 7, 26), 'gustavofelix@gmail.com')
    contato2: Pessoa = Pessoa('Enilda', date(1979, 7, 26), 'enilda@gmail.com')
    contato3: Pessoa = Pessoa('Bruna', date(2005, 7, 26), 'bruna@gmail.com')

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    agenda.imprimir_agenda()

    agenda.buscar_contato('Bruna')

    agenda.imprimir_contato(2)

    agenda.remover_contato(contato3)

    agenda.imprimir_agenda()
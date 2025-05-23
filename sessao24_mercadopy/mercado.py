import os
from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formeta_float_str_moeda

def limpa_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = [] # Exemplo: Carrinho [ { [codigo, nome, preco]: quantidade }, { [codigo, nome, preco]: quantidade } ]

def main() -> None:
    menu()

def menu() -> None:
    print('================================')
    print('========= Bem-Vindo(a) =========')
    print('========== Félix-Shop ==========')
    print('================================')

    print('Selecione uma das opções abaixo:')
    print('(1) - Cadastrar Produto')
    print('(2) - Listar Produtos')
    print('(3) - Comprar Produto')
    print('(4) - Vizualizar carrinho')
    print('(5) - Fechar Pedido')
    print('(6) - Sair do Sistema')

    opcao: int = int(input(''))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        vizualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida')
        sleep(1)
        limpa_terminal()
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('')

    nome: str = str(input('Informe o nome do produto: '))
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {nome} foi cadastrado com sucesso!')
    sleep(2)
    limpa_terminal()
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('-----------------------------')
        print('----Listagem de Pordutos-----')
        print('-----------------------------')
        for produto in produtos:
            print(produto)
            print('----------')
            sleep(1)
    else:
        print('Ainda não existe qualquer produto cadastrado!')
    sleep(2)
    limpa_terminal()
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('-------------------------------------')
        print('------- Produtos Disponiveis --------')
        print('-------------------------------------')
        print('Informe o Código do produto desejado:')
        print('-------------------------------------')
        for produto in produtos:
            print(produto)
            print('')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado!')
            sleep(2)
            menu()
    else:
        print('Ainda não existe qualquer produto cadastrado!')
    sleep(2)
    limpa_terminal()
    menu()

def vizualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print(f'Produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existe qualquer produto no carrinho.')
        sleep(2)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0.0

        print('Produtos do carrinho')
        print('--------------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('----------')
                sleep(1)
        print(f'Sua fatura é de {formeta_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existe qualquer produto no carrinho!')
    sleep(2)
    limpa_terminal()
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
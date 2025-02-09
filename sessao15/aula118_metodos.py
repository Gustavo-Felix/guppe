"""
# Exemplo 01 - Metodo de Instancia
p1 = Produto('Playstation 5', 'Video Game', 3000)

print(p1.desconto(50))
print(Produto.desconto(p1, 50)) # p1 se torna o self, que resulta em Produto.desconto(self, porcentagem)

user1 = Usuario('Gustavo', 'Felix', 'gustavofelix@gmail.com', 'hjghdgshjgjdhag')

print(user1.nome_completo())

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
email = str(input('Digite seu e-mail: '))
senha = input('Digite sua Senha: ')
confirma_senha = input('Confirme sua Senha: ')

if senha == confirma_senha:
    user_teste = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha incorreta!')
    exit(42)

print('Usuario Criado com Sucesso')

senha = input('Informa Sua Senha para acesso: ')

if user_teste.checar_senha(senha):
    print('Acesso Permitido!')
else:
    print('Acesso Negado!')

print(f'Senha Criptografada: {user_teste.mostra_senha()}')

user = Usuario('Gustavo', 'Felix', 'gustavofelix@gmail.com', '123456')

Usuario.conta_usuarios() # forma Correta
user.conta_usuarios() # Possivel, mas não correto

"""
from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o Valor Do Produto Juntamente com o Desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls): # cls é literalmente a classe nam qual está vinculada
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} Usuário(s) no Sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR444'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário Criado: {self.__gera_usuario()}')

    def nome_completo(self):
        """Retorna o Nome Completo"""
        return f'{self.__nome} {self.__sobrenome}'

    def mostra_senha(self):
        """Retorna a Senha do Usuario"""
        return self.__senha

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

# Método Estático

"""
print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Gustavo', 'Felix', 'gustavofelix@gmail.com', '123456')

print(user.contador)
print(user.definicao())
"""


nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
email = str(input('Digite seu e-mail: '))
senha = input('Digite sua Senha: ')
confirma_senha = input('Confirme sua Senha: ')

if senha == confirma_senha:
    user_teste = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha incorreta!')
    exit(42)

print('Usuario Criado com Sucesso')

senha = input('Informa Sua Senha para acesso: ')

if user_teste.checar_senha(senha):
    print('Acesso Permitido!')
else:
    print('Acesso Negado!')

print(f'Senha Criptografada: {user_teste.mostra_senha()}')
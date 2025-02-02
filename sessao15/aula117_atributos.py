# Exemplo 01 - atributo de Instancia

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Publicos e Privados = __atributo = Privado     atributo = Publico

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)

user = Acesso('djkshdsjkd@gmail.com', '12345678')

# user.mostra_email()
# user.mostra_senha()

# print(user.email)
# print(user._Acesso__senha)


# Exemplo 02 - Atributo de classe -

class Produto:

    # Atributo de Classe - Em java, sao chamados de atributos estáticos
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # Atributo de Instancia
        self.nome = nome # Atributo de Instancia
        self.descricao = descricao # Atributo de Instancia
        self.valor = (valor * Produto.imposto) # Atributo de Instancia
        Produto.contador = self.id # Atributo de Instancia




"""

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox Series X', 'Video Game', 2600)


print(p1.imposto) # Forma nao recomendavel para acessar um Atributo de classe
print(p2.imposto) # Forma nao recomendavel para acessar um Atributo de classe

print(Produto.imposto) # Forma Correta

print(p1.id)
print(p2.id)

"""

# Atributo Dinâmicos -> Atributo de Instancia criado em execução

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo Dinâmico

p2.peso = '5Kg' # Note, que não existe peso na classe Produto()

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando Atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print('Deletando...')
print(p1.__dict__)
print(p2.__dict__)

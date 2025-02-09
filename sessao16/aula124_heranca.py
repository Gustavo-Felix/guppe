"""
# Exemplo 01

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    # Cliente herda Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma Não-Comum
        self.__renda = renda

class Funcionario(Pessoa):
    # Funcionario herda Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma Comum
        self.__matricula = matricula


c1 = Cliente('Gustavo', 'felix', '2222222222', 5000)
f1 = Funcionario('Gustavo', 'Felix', '11111111111', 1234)

print(c1.nome_completo())
print(f1.nome_completo())
print(c1.__dict__)
print(f1.__dict__)


"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """
    Cliente herda Pessoa
    """
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma Não-Comum
        self.__renda = renda

class Funcionario(Pessoa):
    """
    Funcionario herda Pessoa
    """
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma Comum
        self.__matricula = matricula


# Overriding - Sobrescrita de Métodos

c1 = Cliente('Gustavo', 'felix', '2222222222', 5000)
f1 = Funcionario('Gustavo', 'Felix', '11111111111', 1234)













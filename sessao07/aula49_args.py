"""
def soma_todos(num1 = 1, num2 = 2, num3 = 3, num4 = 4):
    return num1 + num2 + num3 + num4

print(soma_todos(4, 6 ,9))

print(soma_todos(4, 6))

print(soma_todos(4, 6, 3, 9))


# Entendendo o *args

def soma_todos(nome, email, *args):
    return sum(args), nome, email
    total = 0
    for numero in args:
        total += numero
    return total


print(soma_todos('aa', 'bb'))

print(soma_todos('aa', 'bb', 1))

print(soma_todos('aa', 'bb',2, 3))

print(soma_todos('aa', 'bb',2, 3, 4))

print(soma_todos('aa', 'bb',2, 3, 4, 5))

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza do que você é...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""

def soma_todos(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos(*numeros))













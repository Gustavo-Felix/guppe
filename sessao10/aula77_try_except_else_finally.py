"""
# Exemplo Try

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto!')
except NameError:
    print('Valor incorreto!')
else:
    print(f'Voce digitou {num}')

# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Voce digitou {num}')
finally: # Executa sempre, independente se houver exceção ou não
    print('Final')

# Exemplo mais complexo

def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe um numero: '))
    num2 = int(input('Informe um outro numero: '))
except ValueError:
    print('O Valor precisa ser númerico!')
else:
    print(dividir(num1, num2))

# Outro Exemplo - genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro!'


num1 = input('Informe um numero: ')
num2 = input('Informe um outro numero: ')

print(dividir(num1, num2))
"""

# Outro Exemplo -

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um Problema: {err}'

num1 = input('Informe um numero: ')
num2 = input('Informe um outro numero: ')

print(dividir(num1, num2))










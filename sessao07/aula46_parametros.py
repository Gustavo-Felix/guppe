"""
# Refatoração

def quadrado(num):
    return num ** 2

print(quadrado(7))

def soma(a, b):
    return a + b

print(soma(5, 7)) # Não pode possui mais valores do que parametros
"""

def soma_impares(nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total = total + num
    return total

lista = list(range(0, 8))
if __name__ == '__main__':
    print(soma_impares(lista))
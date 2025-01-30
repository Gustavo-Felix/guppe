"""
# Exemplo All

print(all([0, 1, 2, 3, 4])) # Se Todos os elementos são verdadeiros - False, por causa do '0' no iterável
print(all([1, 2, 3, 4])) # Se Todos os elementos são verdadeiros - True, por estar com todos os elementos verdadeiros
print(all('Gustavo')) # True
print(all([]))

nomes = ['Carlos', 'Camila', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# OBS: O all, entende o iteravel vazio como True
print(all([letra for letra in 'eioq' if letra in 'qwp']))

print(all([num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 1]))
"""

# Exemplo Any

nomes = ['Carlos', 'Camila', 'Cristina', 'Gustavo']

print(any([0, False, {}, (), [], (1)]))

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 5, 6, 7, 8, 9] if num % 2 == 0]))









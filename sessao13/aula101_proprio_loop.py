"""
# Exemplo 01

for num in [1, 2, 3, 4, 5, 6]:
    print(f'{num}')

iter([1, 2, 3, 4, 5, 6])
"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Geek University')


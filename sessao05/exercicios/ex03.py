"""
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).
"""

# Forma 01

for num in range(0, 100000+1, 1000):
    print(num)

# forma 02

num = 0

while num < 100000:
    num += 1000
    print(num)
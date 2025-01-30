'''
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
'''
import math

num1 = int(input("Digite Seu Número:"))

if num1 > 0:
    print(math.sqrt(num1))
elif num1 == 0:
    print("O número Digitado é 0!")
else:
    print("O Número Digitado é Inválido!")
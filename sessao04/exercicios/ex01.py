# 1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

numero1 =  int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print("O Primeiro Número é maior!", numero1)
elif numero1 == numero2:
    print("Os Números São Iguais!")
else:
    print("O Segundo Número é maior!", numero2)
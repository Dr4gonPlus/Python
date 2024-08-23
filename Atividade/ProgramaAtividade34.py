# 34 Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero = int(input('Digite um numero'))

num = int(input('Digite um número: '))

if num < 0:
    print('O número é negativo')
elif num > 0:
    print('O número é positivo')
else:
    print('O número é o 0')
# 40 Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

if num1 == num2 and num2 == num3:
    print('Todos os números são iguais.')

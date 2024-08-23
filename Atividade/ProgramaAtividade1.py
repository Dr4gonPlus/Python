#1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").

numero = int(input('informe o numero \n'))

if (numero == 1):
    print('numero um')
elif (numero == 2):
    print('numero dois')
elif (numero == 3):
    print('numero tres')
else:
    print('numero invalido')
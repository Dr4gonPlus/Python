# 35 Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

verificador = num1 * num2

if verificador == 20:
    print('A multiplicação dos valores inseridos é 20!')
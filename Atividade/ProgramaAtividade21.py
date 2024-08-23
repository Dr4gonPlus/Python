# 21 Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

numero = int(input('digite um numero: \n'))

if (numero <= 9):
    print('menor que 10')
elif (numero == 10):
    print('igual a 10')
elif (numero >= 10):
    print('maior que 10')
# 37 Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.

num = int(input('Digite um número: \n'))

if (num % 2 == 0) or (num % 5 == 0):
    print('O número é multiplo de 2 ou de 5')
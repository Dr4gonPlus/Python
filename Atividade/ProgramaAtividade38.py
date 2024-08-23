# 38 Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.

altura = float(input('informe sua altura: \n'))

if (altura >= 1.75):
    print('Um gigante')
elif (altura <= 1.74):
    print('Um gnomo')
elif (altura > 2.30):
    print('Algo de errado não esté certo')

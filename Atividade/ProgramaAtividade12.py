# 12 Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

print(' bike' )
print(' carro' )
print(' pe' )

modo = str(input(' \n informe sou modo de transporte: \n'))

if (modo == 'bike'):
    print('25 km/h')
if (modo == 'carro'):
    print('100 km/h')
if (modo == 'pe'):
    print('3,6 km/h')
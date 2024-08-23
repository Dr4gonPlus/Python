# 16 Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustível = str(input('escolha entre os tipos de combustiveis: \n'))

if (combustível == 'gasolina'):
    print('6,19 o litro')
elif (combustível == 'diesel'):
    print('5,95 o litro')
elif (combustível == 'etanol'):
    print('4.08 o litro')
else:
    print('Invalido')
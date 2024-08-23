# 13 Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input('Digite o mês que você deseja: '))

if (mes >= 1 and mes <= 2) or mes == 12:
    print('Estamos no verão! ')
elif mes >= 3 and mes <= 5:
    print('Estamos no outono!')
elif mes >= 6 and mes <= 8:
    print('Estamos no inverno!')
elif mes >= 9 and mes <= 11:
    print('Estamos na primavera!')
else:
    print('Este mês não existe.')
# 7 Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando match-case.

Nota = int(input('Digite sua nota:'))

match Nota:
    case 1:
        print('Nota baixa')
    case 2:
        print('Nota baixa')
    case 3:
        print('Nota baixa')
    case 4:
        print('Nota baixa')
    case 5:
        print('Nota baixa')
    case 6:
        print('Nota media')
    case 7:
        print('Nota media')
    case 8:
        print('Nota media')
    case 9:
        print('Nota alta')
    case 10:
        print('Nota alta')
    case _:
        print('Numero invalido')        
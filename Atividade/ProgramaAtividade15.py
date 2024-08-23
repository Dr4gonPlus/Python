# 15 Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 19 anos).

idade = int(input('qual sua idade: \n'))

if (idade >= 13 and idade <= 17):
    print('adolescente')
elif (idade == 18 and 19):
    print('maior de idade')
else:
    print('adulto')
# 6 Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

calculo = int(input('quanto é 43+43? \n'))

def calculo(a, b):
    return a + b

resultado = calculo(43, 43)
print(f'resultado: {resultado}')
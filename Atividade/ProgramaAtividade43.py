# 43 Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

vezes = int(input('Digite a quantidade de vezes que a mensagem será exibida: '))

for i in range(vezes + 1):
    print(f'{i}° vez que esta mensagem é exibida')
# 47 Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

num = int(input('Digite um número: '))

print(f'A tabuada do número {num} é: ')
for i in range(10):
    print(f'{i + 1} X {num} = {num * (i + 1)}')
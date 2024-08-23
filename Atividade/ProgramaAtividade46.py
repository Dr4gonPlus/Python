# 46 Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

total = 0

for i in range(10):
    num = int(input(f'Digite o {i + 1}° número: '))
    total += num

print(f'A média total da soma de todos os números inceridos é: {total / 2}')
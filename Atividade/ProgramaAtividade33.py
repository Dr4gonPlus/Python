# 33 Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

value = float(input('Digite o valor do produto: '))

print(f'O valor do produto com o disconto de 10% é: R${value + (value * (10 / 100))}')
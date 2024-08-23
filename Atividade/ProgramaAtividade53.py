# 53 Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

import time


num = int(input('Digite um número para uma contagem: '))

for i in range(num, 0, -1): 
    print(i)
    time.sleep(1)
print('Fim da contagem')
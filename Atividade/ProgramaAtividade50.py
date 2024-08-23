# 50 Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.

num = int(input('Digite um número para uma contagem: '))

for i in range(num, 0, -1): 
    print(i)
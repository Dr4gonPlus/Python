# 45 Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

maior = None
for i in range(5):
    num = int(input('Digite um número: '))
    
    if maior < num or maior is None:
        maior = num

print(f'O maior número digitado foi: {maior}')
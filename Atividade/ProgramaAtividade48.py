# 48 Escreva um algoritmo que solicite ao usuário uma palavra e exiba cada letra da palavra em uma linha separada.

word = input('Digite uma palavra: ').upper()

for i in range(len(word)):
    print(word[i])
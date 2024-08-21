#4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

Cores = int(input('Informe uma cor:'))

Cor = ['vermelho', ' verde', 'azul']


match Cores:
    case vermelho:
        print("Você escolheu vermelho")
    case verde:
        print("Você escolheu verde")
    case azul:
        print('Você escolheu azul')
    case _:
        print('Cor invalida')

for cor in cores:
    print(cor)

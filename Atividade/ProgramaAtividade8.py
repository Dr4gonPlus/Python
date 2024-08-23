# 8 Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

print( '\n 1.Casado \n', '2.Divorciado \n', '3.Viúvo \n', '4.Solteiro \n')

Estado_civil = int(input('Informe seu estado civil: \n ' ))

if (Estado_civil == 1):
    print('Usuario casado')
elif (Estado_civil == 2):
    print('Usuario divorciado')
elif (Estado_civil == 3):
    print('Usuario viúvo')
elif (Estado_civil == 4):
    print('Usuario solteiro')
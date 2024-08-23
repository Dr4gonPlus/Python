# 39 Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".

senha = int(input('Digite uma senha de 4 digitos'))

if senha == 1234:
    print('Sua senha é muito manjada!')
else:
    print('Wow que senha forte!')
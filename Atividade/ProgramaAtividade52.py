# 52 Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

senha_correta = '123'

while True:
    senha = input('Digite a senha: \n')
    if senha == senha_correta:
        print('senha correta')
        break
    else:
        print('senha incorreta')

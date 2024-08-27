#numero1 = int(input('Informe o numero: \n'))
#numero2 = int(input('Informe o numero: \n'))

#print('A some é: ', numero1 + numero2)


#numeros = [1, 5, 8, 10, 3, 78, 100]

#print(max(numeros)) # mostra o maior numero da minha lista
#print(min(numeros)) # mostra o menor numero da minha lista
#print(len(numeros)) # mostra a quantidade de itens que tem na minha lista 
#print(sum(numeros)) # soma todos os numeros da minha lista

#media = sum(numeros) / len(numeros)

#print(media)
#
# def resultado (numero1, numero2):
#    resultado = numero1 / numero2
#    return resultado
#
# resultado = soma(12, 12)
#
# print(resultado)



#resposta = media(numeros)
#
#print(resposta)

#numeros = [0, 1, 2, 4, 5, 7, 9]

# def soma (a, b) :
#    soma = a * b
#    return soma 
#
#print(soma)


# uso da função soma 
#print(soma(15, 35))

# função sem retorno
# def saudacao(nome):
#    print(f'Olá {nome}')


# def ola(nome, mensagem='Olá'):
#    print(mensagem + nome)

#ola(' Jó', 'oi')
#ola(' Jó')

# função com multiplo retorno

# def dividir (numero1 , numero2 ):
#    resposta = numero1 // numero2
#    resto = numero1 % numero2 
#    return resposta, resto

#divisao = dividir(10, 2) 

#print(divisao)
##print(resto_divisao)

#numeros = [1 ,2, 3, 5, 7,]

#print(type(numeros))



# função que recebe dois numeros e soma

# def soma (numero1, numero2):
#    soma = numero1 + numero2
#    return soma 

#somar = lambda numero1, numero2: numero1 + numero2

#print(somar(10,5))

def exibir_informacoes(*args):
    print('argumentos posicionais: ', args)

exibir_informacoes(1,2,'Jo', 'Teste')

def exibir_informacoes2(**args):
    print('Argumentos posicionais: ', args)

exibir_informacoes2(nome='Jo', idade=20, curso='python')

# key : value
# chave : valor

pessoas =[{
    'nome': 'Jó',
    'idade': 20,
    'estado_civil': 'solteiro',
    'escolaridade': 'especialista'
},
{
    'nome': 'Raphael',
    'idade': 16,
    'estado_civil': 'noivo',
    'escolaridade': 'fudido'
}]

print(pessoas[1])
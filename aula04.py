numero1 = int(input('Informe o primeiro numero \n'))
numero2 = int(input('Informe o segundo numero \n'))

print(numero1 + numero2)
print(type(numero1))
print(type(numero2))


nome = 'Jó'
idade = 20
altura = 1.92
vivo = False

# int()
# float()
# str()
# bool()

print(int(vivo))

print(type(nome))
print(type(str(idade)))
print(type(altura))
print(type(vivo))

numero1 = int(input('Informe o primeiro numero \n'))
numero2 = int(input('Informe o segundo numero \n'))

soma = numero1 + numero2 
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

#print(soma)
#print(subtracao)
#print(multiplicacao)print(divisao)

print('A some é: ', soma )
print('A subtracao é: '+ str(subtracao))
print('A multiplicacao é: {} e a divisao foi {}'.format(multiplicacao, divisao) )

nome = 'Jó'
sobrenome = 'Nunes'

print('O seu nome completo é '+ nome +' '+ sobrenome)
print('O seu nome completo é', nome , sobrenome)
print('O seu nome completo é (nome) (sobrenome) ')

# Informe 10 informações de cadastro pessoal e informe um relatorio com as informações em um unico print.
# Calcule a area de um trinagulo fornecendo somente base e altura
# Crie um algoritimo capaz de calcular o delta da formula de bascara

#10 informações de cadastro pessoal

nome = str(input('Informe o nome \n'))
data_de_nascimento = str(input('Informe a data de nascimento \n'))
sexo = str(input('Informe seu sexo \n'))
endereço = str(input('Informe seu endereço \n'))
cidade = str(input('Informe sua cidade \n'))
estado = str(input('Informe seu estado \n'))
cep = str(input('Informe seu cep \n'))
telefone = str(input('Informe o seu telefone \n'))
email = str(input('Informe o email \n'))
nacionalidade = str(input('Informe sua nacionalidade \n'))

#Exemplo com base e altura fornecidas

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
area = (base * altura) / 2 

print(f"A área do triângulo é {area:.2f} unidades de área.")

#Cálculo do delta na fórmula de Bhaskara

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if a == 0:
    print("O valor de 'a' deve ser diferente de zero.")
elif delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"Raiz 1 (x1): {x1:.2f}")
    print(f"Raiz 2 (x2): {x2:.2f}")




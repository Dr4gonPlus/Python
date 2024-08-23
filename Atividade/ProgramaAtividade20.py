# 20 Crie um programa que solicite ao usuário a temperatura em graus Celsius e converta para Fahrenheit.

celsius = float(input('informe a temperatura: \n'))

fahrenheit = (celsius * 1.8) + 32

print(f"{celsius:.1f}°C é igual a {fahrenheit:.1f}°F")
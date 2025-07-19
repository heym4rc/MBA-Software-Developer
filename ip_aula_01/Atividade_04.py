# Escreva um programa em Python que solicite ao usuário uma temperatura em graus Celsius
# e faça a conversão para Fahrenheit. Exiba o resultado na tela.

temp_c = float(input('Digite a temperatura em Celsius:'))
temp_f = temp_c * 1.8 + 32

print(f'A temperatura em Fahrenheit {temp_f: .2f}')
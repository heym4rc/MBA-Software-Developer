# Escreva um programa em Python que solicite ao usuário a largura e a altura de um retângulo.
# Calcule a área desse retângulo e exiba o resultado.

#Variaveis
largura = float(input('Qual a largura do retângulo?'))
altura = float(input('Qual a altura do retângulo?'))

area = largura * altura

print(f'A área do retângulo é {area: .2f}')
# Exercício da Média: Escreva um programa em Python que solicite ao usuário
# duas notas e calcule a média entre elas. Em seguida, exiba o resultado na tela

nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
media = (nota1 + nota2) / 2

print(f'A média do estudante é {media: .2f}')
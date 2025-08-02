# Um programa que gera a tabuada completa de qualquer número.
# O usuário escolhe o número e o programa exibe a tabuada de 1 a 10

numero = int(input("Digite um número para gerar a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
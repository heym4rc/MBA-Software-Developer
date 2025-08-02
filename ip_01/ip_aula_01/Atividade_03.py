# Exercício do Desconto: Escreva um programa em Python que solicite
# ao usuário o valor de um produto e o percentual de desconto.
# Calcule o valor do desconto e exiba o valor final após o desconto.

#Variaveis
valor = float(input('Qual o valor do produto:'))
percentual = float(input('Qual o percentual de desconto do produto?'))

#Funções e Métodos

#Processamento
desconto = valor - (valor * percentual / 100)

#Vizualização
print(f'O desconto do produto é:{desconto}')
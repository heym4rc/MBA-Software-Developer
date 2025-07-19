# Programa para Calcular o Indice de Massa Corporal (IMC)

# Solicita ao usuário o peso e a altura
# Usamos .replace(',', '.') para aceitar tanto ponto quanto vírgula
# como separador decimal, tornando o programa mais flexível para o usuário.
peso_str = input('Digite seu peso em kg (ex: 70.5): ')
peso = float(peso_str.replace(',', '.'))
altura_str = input('Digite sua altura em metros (ex: 1.73): ')
altura = float(altura_str.replace(',', '.'))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f'Seu IMC é: {imc:.2f}')  # Exibe o resultado formatado com duas casas decimais
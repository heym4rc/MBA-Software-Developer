# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição.

# Solicita o peso e a altura do usuário
peso_str = input('Digite seu peso em kg (ex: 70.5): ')
peso = float(peso_str.replace(',', '.'))
altura_str = input('Digite sua altura em metros (ex: 1.73): ')
altura = float(altura_str.replace(',', '.'))

# Valida a altura para evitar divisão por zero
if altura <= 0:
    print("Altura inválida. Por favor, insira um valor positivo para a altura.")
else:
    # Calcula o IMC
    imc = peso / (altura ** 2)

    print(f"Seu IMC é {imc:.2f}.")

    # Verifica a condição do IMC com base nos padrões da OMS
    if imc < 18.5:
        print("Você está Abaixo do Peso.")
    elif imc < 25:
        print("Você está no Peso Normal.")
    elif imc < 30:
        print("Você está com Sobrepeso.")
    elif imc < 35:
        print("Você está com Obesidade Grau I.")
    elif imc < 40:
        print("Você está com Obesidade Grau II.")
    else:  # imc >= 40
        print("Você está com Obesidade Grau III.")